from django.contrib import admin
from .models import contact,projectscount,projectsphoto
# Register your models here.
admin.site.register([contact,projectsphoto,projectscount])