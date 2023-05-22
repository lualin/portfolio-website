from django.shortcuts import render

# Create your views here.

def login(request):
    return render(
        request, 
        'single_pages/login.html')

def register(request):
    return render(
        request, 
        'single_pages/register.html')

def home(request):
    return render(
        request,
        'single_pages/home.html'
    )
        
def about(request):
    return render(
        request,
        'single_pages/about.html'
    )