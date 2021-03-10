
from django.shortcuts import render

# Create your views here.

def service(request):
    return render(request ,'services.html')

def new(request):
    return render(request ,'gallery.html')
def about(request):
    return render(request ,'about.html')
def contact(request):
    return render(request ,'contact.html')
