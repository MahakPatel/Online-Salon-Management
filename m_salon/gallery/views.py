from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request ,'gallery.html')
def service(request):
    return render(request,'service.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def home(request):
    return render(request,'index.html')
