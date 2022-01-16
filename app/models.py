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

class Collaborations(models.Model):
    image = models.ImageField(upload_to='Collaborations/images/')
    name = models.CharField(max_length=1000)
    pageContent = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

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

class WorkerLoan(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=1000)
    BusinessName = models.CharField( max_length=1000)
    WorkType = models.CharField( max_length=1000)
    AadharNo = models.CharField( max_length=1000)
    PanNo = models.CharField( max_length=1000)
    Contact = models.CharField( max_length=1000)
    email = models.CharField( max_length=1000)
    Address = models.TextField()
    accountHolderName = models.CharField(max_length=1000)
    accountNo = models.CharField(max_length=250)
    IFSC_Code = models.CharField(max_length=250)
    IFSC_Branch = models.CharField(max_length=250)
    Que1 = models.CharField(max_length=1000,default="Have you taken a loan previously?")
    Ans1 = models.CharField(max_length=1000)
    Que2 = models.CharField(max_length=1000, default="Do you need loan?")
    Ans2 = models.CharField(max_length=1000)
    Que3 = models.CharField(max_length=1000, default="Have you filed your ITR for last 3 years?")
    Ans3 = models.CharField(max_length=1000)
    Que4 = models.CharField(max_length=1000, default="Do you have your CIBIL report?")
    Ans4 = models.CharField(max_length=1000)
    Que5 = models.CharField(max_length=1000, default="Does your bank send you the bank statement on email?")
    Ans5 = models.CharField(max_length=1000)
    Que6 = models.CharField(max_length=1000, default="last 1 year turnover?")
    Ans6 = models.CharField(max_length=1000)
    Que7 = models.CharField(max_length=1000, default="Do you have Udyog Aadhar Shop Act License?")
    Ans7 = models.CharField(max_length=1000)
    Que8 = models.CharField(max_length=1000, default="Do you live on rent? Do you have a rent agreement?")
    Ans8 = models.CharField(max_length=1000)
    Que9 = models.CharField(max_length=1000, default="For 1 Lakh Rupees to 25 Lakh Rupees loan, do you have a project report and a training done?")
    Ans9 = models.CharField(max_length=1000)

class Worker(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=1000)
    BusinessName = models.CharField( max_length=1000)
    WorkType = models.CharField( max_length=1000)
    AadharNo = models.CharField( max_length=1000)
    PanNo = models.CharField( max_length=1000)
    Contact = models.CharField( max_length=1000)
    email = models.CharField( max_length=1000, null=True)
    Address = models.TextField()
    accountHolderName = models.CharField(max_length=1000)
    accountNo = models.CharField(max_length=250)
    IFSC_Code = models.CharField(max_length=250)
    IFSC_Branch = models.CharField(max_length=250)
    Que1 = models.CharField(max_length=1000,default="Since how long are you doing this work?")
    Ans1 = models.CharField(max_length=1000)
    Que2 = models.CharField(max_length=1000, default="what is your annual turnover?")
    Ans2 = models.CharField(max_length=1000)
    Que3 = models.CharField(max_length=1000, default="Do you do cashless transactions?")
    Ans3 = models.CharField(max_length=1000)
    Que4 = models.CharField(max_length=1000, default="Are you wiling to take a contract? what is the maximum contract amount?")
    Ans4 = models.CharField(max_length=1000)
    Que5 = models.CharField(max_length=1000, default="How early can you serve the customer after receiving a call or message?")
    Ans5 = models.CharField(max_length=1000)
    


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


class HomeImage(models.Model):
    image = models.ImageField(upload_to='HomeImage/images/')

class BusinessOwner(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=1000)
    BusinessName = models.CharField( max_length=1000)
    WorkType = models.CharField( max_length=1000)
    AadharNo = models.CharField( max_length=1000)
    PanNo = models.CharField( max_length=1000)
    Contact = models.CharField( max_length=1000)
    email = models.CharField( max_length=1000)
    Address = models.TextField()
    accountHolderName = models.CharField(max_length=1000)
    accountNo = models.CharField(max_length=250)
    IFSC_Code = models.CharField(max_length=250)
    IFSC_Branch = models.CharField(max_length=250)

class DistrictHandler(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=1000)
    AadharNo = models.CharField( max_length=1000)
    PanNo = models.CharField( max_length=1000)
    Contact = models.CharField( max_length=1000)
    email = models.CharField( max_length=1000)
    Address = models.TextField()
    profilepic = models.ImageField(upload_to='DistrictHandler/')
    accountHolderName = models.CharField(max_length=1000)
    accountNo = models.CharField(max_length=250)
    IFSC_Code = models.CharField(max_length=250)
    IFSC_Branch = models.CharField(max_length=250)


class TalukaHandler(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=1000)
    AadharNo = models.CharField( max_length=1000)
    PanNo = models.CharField( max_length=1000)
    Contact = models.CharField( max_length=1000)
    email = models.CharField( max_length=1000)
    profilepic = models.ImageField(upload_to='TalukaHandler/')
    Address = models.TextField()
    accountHolderName = models.CharField(max_length=1000)
    accountNo = models.CharField(max_length=250)
    IFSC_Code = models.CharField(max_length=250)
    IFSC_Branch = models.CharField(max_length=250)

class M_Operator(models.Model):
    StateID = models.ForeignKey(StateIND, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    TalukaID = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    CityVillageID = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=1000)
    AadharNo = models.CharField( max_length=1000)
    PanNo = models.CharField( max_length=1000)
    Contact = models.CharField( max_length=1000)
    email = models.CharField( max_length=1000)
    profilepic = models.ImageField(upload_to='M_Operator/')
    Address = models.TextField()
    accountHolderName = models.CharField(max_length=1000)
    accountNo = models.CharField(max_length=250)
    IFSC_Code = models.CharField(max_length=250)
    IFSC_Branch = models.CharField(max_length=250)






