from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Contact
from django.utils import timezone
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render (request, 'home/about.html')

def projects(request):
    return render(request, 'home/projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        pub_date = timezone.now()
        contact_info = Contact(name=name,email=email,message=message,post_date=pub_date)
        contact_info.save()
        print("Entry added to DB")
        return HttpResponseRedirect(reverse('home:contact'))


    else:
        return render(request, 'home/contact.html')
 



