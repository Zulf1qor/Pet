from django.db import models
from django.core.validators import RegexValidator

class Social(models.Model):
    twitter = models.CharField(max_length=155)
    facebook = models.CharField(max_length=155)
    inlink = models.CharField(max_length=155)
    instagramm = models.CharField(max_length=155)


class Banner(models.Model):
    title = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    addtion = models.CharField(max_length=55)
    image = models.ImageField(upload_to='banner_imageh/')
    image2  = models.ImageField(upload_to='banner_imageh2/')


class Service(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=155)


class About(models.Model):
    title = models.CharField(max_length=25)
    addition = models.CharField(max_length=100)
    description = models.CharField(max_length=155)
    image = models.ImageField(upload_to='About_image/')
    image2 = models.ImageField(upload_to='About_image2/')
    image3= models.ImageField(upload_to='About_image3/')


class Advantages(models.Model):
    title = models.CharField(max_length=155)


class Choose(models.Model):
    title = models.CharField(max_length=25)
    addition = models.CharField(max_length=155)
    image = models.ImageField(upload_to='image_choose/')


class Pricing(models.Model):
    title = models.CharField(max_length=55)
    price = models.FloatField()
    image = models.ImageField(upload_to='pricing_image/')
    feeding = models.BooleanField(default=0)
    boarding = models.BooleanField(default=0)
    spa_grooming = models.BooleanField(default=0)
    veterinary_medicine = models.BooleanField(default=0)


class Team(models.Model):
    image = models.ImageField(upload_to='team_image/')
    name = models.CharField(max_length=55)
    job = models.CharField(max_length=55)
    social = models.ForeignKey(to='Social', on_delete=models.CASCADE)


class Testimonial(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='Image_testimonial/')
    profeccion = models.CharField(max_length=55)
    about = models.CharField(max_length=155)


class Blog(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='blog_image/')
    profession = models.CharField(max_length=55)
    own = models.CharField(max_length=55)
    description = models.CharField(max_length=255)


class Contact(models.Model):
    name = models.CharField(max_length=25)
    surename = models.CharField(max_length=25)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()



