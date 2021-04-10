from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from payment import Checksum
from django.views.decorators.csrf import csrf_exempt
from Staff.models import Staff
from appoinment.models import Booking
from home.models import register
from services.models import service
from .filters import OrderFilter
from .forms import OrderForm, CustomerForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
MERCHANT_KEY = 'jYeGkvD385PQPBeD'


# Create your views here.
def dashboard(request):
    Bookings = Booking.objects.all()
    customers = register.objects.all()
    total_customers = customers.count()
    total_Bookings = Booking.objects.count()
    Booked = Booking.objects.filter(status='Booked').count()
    pending = Booking.objects.filter(status='Pending').count()
    context = {'orders': Bookings, 'customers': customers,
               'total_orders': total_Bookings, 'Booking': Booked,
               'pending': pending}

    return render(request, 'dashboard.html', context)


def customer(request, pk_test):
    customer = register.objects.get(id=pk_test)
    Bookings = customer.booking_set.all()
    myFilter = OrderFilter(request.GET, queryset=Bookings)
    Bookings = myFilter.qs
    Bookings_count = Bookings.count()
    print(customer, Bookings, Bookings_count)
    context1 = {'customer': customer, 'orders': Bookings, 'order_count': Bookings_count, 'myFilter': myFilter}
    return render(request, 'customer.html', context1)


def dash_services(request):
    ser = service.objects.all()
    return render(request, 'dash_service.html', {'service': ser})


def dash_staff(request):
    staff = Staff.objects.all()
    return render(request, 'dash_staff.html', {'staff': staff})


def updateOrder(request, pk):
    order = Booking.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            templete = render_to_string('update_email.html', {'name': request.user.register.username,'status':Booking.status})
            send_mail('Appoinment is Booked',
                     templete,
                      settings.EMAIL_HOST_USER,
                      [request.user.register.email], fail_silently=False)
            return redirect('/dashboard')


    context = {'form': form}
    return render(request, 'order_form.html', context)

@login_required(login_url='loginhandle')
def deleteOrder(request, pk):
    order = Booking.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/dashboard')

    context = {'item': order}
    return render(request, 'delete.html', context)

@login_required(login_url='adminlogin')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(register, Booking,
                                         fields=('name', 'email', 'service', 'status', 'date', 'time'), extra=1)
    customer = register.objects.get(id=pk)
    formset = OrderFormSet(queryset=Booking.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            param_dict = {

                'MID': 'CMHljw77603804792614',
                'ORDER_ID': '65',
                'TXN_AMOUNT': '100',
                'CUST_ID': 'mahakpatel0208@gmail.com',
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/dashboard/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'paytm.html', {'param_dict': param_dict})

    context = {'form': formset}
    return render(request, 'order_form.html', context)


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum1 = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum1)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

@login_required(login_url='loginhandle')
def userPage(request):
    orders = request.user.register.booking_set.all()

    total_Bookings = orders.count()

    Booked = orders.filter(status='Booked').count()
    pending = orders.filter(status='Pending').count()

    customer = register.objects.all()
    print(customer)

    context = {'orders': orders, 'total_orders': total_Bookings,
               'Booking': Booked, 'pending': pending, 'customer': customer}
    return render(request, 'user.html', context)

@login_required(login_url='loginhandle')
def accountSettings(request):
    customer = request.user.register
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile Updated Successfully')


    context = {'form': form}
    return render(request, 'account_setting.html', context)
