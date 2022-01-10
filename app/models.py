from django.db import models

# Create your models here.

class ImageSlider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class IndiPageContent(models.Model):
    page = models.CharField(max_length=256)
    pageContent = models.TextField()
    def __str__(self):
        return self.page

class appDocuments(models.Model):
    title = models.CharField(max_length=1000, default="Document")
    document4 = models.FileField(upload_to='Documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Advertisements(models.Model):
    title = models.CharField(max_length=1000, default="Document")
    image = models.ImageField(upload_to='Advertisements/images/')
    pageContent = models.TextField()
    document4 = models.FileField(upload_to='Advertisements/Documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Schemes(models.Model):
    title = models.CharField(max_length=1000, default="Document")
    image = models.ImageField(upload_to='Schemes/images/')
    pageContent = models.TextField()
    document4 = models.FileField(upload_to='Schemes/Documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
