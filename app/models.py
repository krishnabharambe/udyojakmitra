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


class StateIND(models.Model):
    Value = models.CharField(max_length=100)
    Status = models.CharField(max_length=100, default="Inactive")
    def __str__(self):
        return self.Value
        
class District(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    Value = models.CharField(max_length=100)
    Status = models.CharField(max_length=100, default="Inactive")
    def __str__(self):
        return self.Value

class Taluka(models.Model):
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    Value = models.CharField(max_length=100)
    Status = models.CharField(max_length=100, default="Inactive")
    def __str__(self):
        return self.Value

class CityVillage(models.Model):
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    Value = models.CharField(max_length=100)
    Status = models.CharField(max_length=100, default="Inactive")
    def __str__(self):
        return self.Value

class Worker(models.Model):
    fullname = models.CharField(max_length=256)
    address = models.TextField()
    contact = models.CharField(max_length=256)
    Gender = models.CharField(max_length=256)
    DOB = models.CharField(max_length=256)
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)

class Customers(models.Model):
    fullname = models.CharField(max_length=256)
    address = models.TextField()
    contact = models.CharField(max_length=256)
    Gender = models.CharField(max_length=256)
    DOB = models.CharField(max_length=256)
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)


