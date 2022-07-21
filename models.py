from distutils.command.upload import upload
from django.db import models

# Create your models here.
class places(models.Model):
    image=models.ImageField(upload_to='imgs')
    area=models.TextField(max_length=20)
    descr=models.TextField(max_length=100)
    offer=models.BooleanField(default=False)
    amount=models.IntegerField()






class user_details(models.Model):
    number=models.IntegerField()
    from_place=models.TextField(max_length=25)
    to_place=models.TextField(max_length=25)
    number_of_passengers=models.IntegerField()
    arrival_date=models.DateField(auto_now=False, auto_now_add=False)
    leaving_date=models.DateField(auto_now=False, auto_now_add=False)

 
