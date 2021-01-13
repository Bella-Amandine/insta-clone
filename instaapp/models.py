from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='photos/', defautl='default.png')
    

