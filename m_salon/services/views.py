
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



def service1(request):
    return render(request ,'services.html')

def new(request):
    return render(request ,'gallery.html')
def about(request):
    return render(request ,'about.html')
def contact(request):
    return render(request ,'contact.html')
