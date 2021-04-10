from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from appoinment.models import Booking
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from service import Service

from services.models import service

MERCHANT_KEY = 'your merchant key'
# Create your views here.
from appoinment.models import appo, Booking
from payment import Checksum
from home.models import register
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginhandle')
def appoinment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['txtDate']
        time = request.POST['time']
        service = request.POST['service']
        beautician = request.POST['beautician']
        request.session['service'] = service
        id1=Booking.objects.all()
        print(id1)
        if (Booking.objects.filter(date=date).exists() and Booking.objects.filter(time=time).exists() and Booking.objects.filter(beautician=beautician).exists()):
            messages.info(request, "The Beautician is already Booked at this particular Time slot ")
            return render(request, 'appointment.html')
        else:
            x3 = Booking(name=name, email=email, date=date, time=time, service=service,beautician=beautician)
            x3.save()
            templete = render_to_string('email_templete.html',{'name':request.user.register.username,'date':date,'time':time,'service':service,'beautician':beautician,'id':Booking.id})
            send_mail('Thank you for your Appoinment At M&M Salon',
                             templete,settings.EMAIL_HOST_USER,
                             [request.user.register.email],fail_silently=False)

            return redirect('bill')
    else:
        return render(request, 'appointment.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

@login_required(login_url='loginhandle')
def bill(request):
    service1= request.session.get('service')
    bill = service.objects.get(Service=service1)

    print(bill.price)
    return render(request, 'bill.html', {"bill": bill,'u_name':request.user.register.username})

def payment(request):

    service1 = request.session.get('service')
    bill = service.objects.get(Service=service1)
    print(bill)

    param_dict = {

        'MID': 'your merchant id',
        'ORDER_ID': '205',
        'TXN_AMOUNT':str(bill.price),
        'CUST_ID': 'mahakpatel0208@gmail.com',
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'http://127.0.0.1:8000/appoinment/handlerequest/',

    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render(request, 'paytm.html', {'param_dict': param_dict})

