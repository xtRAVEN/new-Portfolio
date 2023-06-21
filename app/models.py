from django.db import models

# Create your models here.


class projectsphoto(models.Model):
    image = models.ImageField(upload_to='images')




class projectscount(models.Model):
    total = models.IntegerField()
    complex = models.IntegerField()
    experience = models.IntegerField()
    



class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    messafe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    