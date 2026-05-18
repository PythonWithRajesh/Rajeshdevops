from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from home.models import Contact

# Home Page
def index(request):
    return render(request, 'index.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Services Page
def services(request):
    return render(request, 'services.html')
    
def icecream(request):
    return render(request, 'icecream.html')

def kulfi(request):
    return render(request, 'kulfi.html')

def badamshake(request):
    return render(request, 'badamshake.html')

def faluda(request):
    return render(request, 'faluda.html')

def hocco(request):
    return render(request, 'hocco.html')

def oreo(request):
    return render(request, 'oreo.html')

def mango(request):
    return render(request, 'mango.html')

def coffe(request):
    return render(request, 'coffe.html')

def familypack(request):
    return render(request, 'familypack.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mess = request.POST.get('mess')

        # Save in database
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=mess
        )

        messages.success(request, "Message saved successfully 🍦 We will contact you soon.")
        return redirect('/contact')

    return render(request, "contact.html")