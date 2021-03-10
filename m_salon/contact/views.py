
from django.shortcuts import render,redirect

# Create your views here.
from contact.models import con
def contact(request):
    return render(request ,'contact.html')

def con(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        message = request.POST['message']
        x5 = con(name=name, email=email,website=website, message=message)
        print(x5)
        x5.save()
        return redirect('/login')

    else:
        return render(request, 'contact.html')