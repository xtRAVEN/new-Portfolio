from django.shortcuts import render
from .models import projectsphoto,projectscount,contact
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')  
        contact.objects.create(email=email,name=name,messafe=message)
        return HttpResponse("your message recieved we'll contact you soon.")
    nav = ['Home','Skills','Projects','Contact']
    photo = projectsphoto.objects.all()
    count = projectscount.objects.all()
    return render(request,'index.html',{'nav':nav,'photo':photo,'count':count})