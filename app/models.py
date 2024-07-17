from django.db import models

# Create your models here.


class projectsphoto(models.Model):
    image = models.URLField()




class projectscount(models.Model):
    total = models.IntegerField()
    complex = models.IntegerField()
    experience = models.CharField(max_length=20)
    



class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    messafe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    