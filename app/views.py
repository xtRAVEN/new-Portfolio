from django.shortcuts import render
from .models import projectsphoto,projectscount,contact
from django.http import HttpResponse
from django.core.cache import cache
from django.shortcuts import render
from django.dispatch import receiver
from django.core.cache import cache
from django.db.models.signals import post_save

@receiver(post_save, sender=(projectsphoto))
def contact_saved(sender, instance, created, **kwargs):
    if created:
        cache.delete('index_data') 
@receiver(post_save, sender=(projectscount))
def contact_saved(sender, instance, created, **kwargs):
    if created:
        cache.delete('index_data') 


        
def index(request):
    # Try to get the cached data
    cached_data = cache.get('index_data')

    if cached_data is None:
        # Data is not in the cache, fetch it from the database
        print("data cached")
        nav = ['Home', 'Skills', 'Projects', 'Contact']
        photo = projectsphoto.objects.all()
        count = projectscount.objects.all()
        
        # Store the data in the cache for future requests
        cache.set('index_data', {'nav': nav, 'photo': photo, 'count': count})
        
    else:
        print("already cached data used ")
        # Use the cached data
        nav = cached_data['nav']
        photo = cached_data['photo']
        count = cached_data['count']
        
       
    if request.method == 'POST':
        # Handle the POST request
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')  
        contact.objects.create(email=email, name=name, message=message)
        return HttpResponse("Your message received. We'll contact you soon.")

    return render(request, 'index.html', {'nav': nav, 'photo': photo, 'count': count})
