from django.db import models

# Create your models here.

class userRegister(models.Model):
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    fullAddress = models.CharField(max_length=50)
    password1 = models.CharField(max_length=30,null=True) #PASSWORD TO BE HASHED
    password2 = models.CharField(max_length=30,null=True)
    #profilePic = models.ImageField(upload_to ='customers_pic/',null=True)

class profRegister(models.Model):
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    fullAddress = models.CharField(max_length=50)
    profilePic = models.ImageField(upload_to ='prof_pic/',null=True)
    password1 = models.CharField(max_length=30,null=True) #PASSWORD TO BE HASHED
    password2 = models.CharField(max_length=30,null=True)
    service_selection=models.BooleanField()
    working_location=models.BooleanField()
    experience=models.IntegerField()
    training_certificate = models.ImageField(upload_to ='training_certificates/',null=True)

    
