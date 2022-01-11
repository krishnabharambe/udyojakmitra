from django.shortcuts import render
from .models import ImageSlider, IndiPageContent, appDocuments as M_appDocuments, Advertisements as M_Advertisements, Schemes as M_Schemes
# Create your views here.
rootUrl = "http://127.0.0.1:8000"

def index(request):
    IS = ImageSlider.objects.all()
    context={'IS':IS,'index':'index'}
    return render(request,"app/index.html",context)

def About_Us(request):
    IPC = IndiPageContent.objects.filter(page="AboutUs").first()
    context={'IPC':IPC,'About_Us':'About_Us'}
    return render(request,"app/About_Us.html",context)

def Regional_List(request):
    context={}
    return render(request,"app/Regional_List.html",context)

def Documents(request):
    ADocuments = M_appDocuments.objects.all()
    context={'ADocuments':ADocuments,"rootUrl":rootUrl,'Documents':'Documents'}
    return render(request,"app/Documents.html",context)

def IndexAdvertisements(request, id):
    ms = M_Advertisements.objects.get(id=id)
    return render(request, 'app/PageView.html',{"rootUrl":rootUrl,'ms':ms,'Advertisements':'Advertisements'})

def Advertisements(request):
    msa = M_Advertisements.objects.all()
    context={'msa':msa,'rootUrl':rootUrl,'Advertisements':'Advertisements'}
    return render(request,"app/Advertisements.html",context)

def IndexSchemes(request, id):
    ms = M_Schemes.objects.get(id=id)
    return render(request, 'app/PageView.html',{"rootUrl":rootUrl,'ms':ms,'Schemes':'Schemes'})

def Schemes(request):
    mSchemes = M_Schemes.objects.all()
    context={'Schemes':'Schemes','msa':mSchemes,'rootUrl':rootUrl}
    return render(request,"app/Schemes.html",context)

def Quick_Links(request):
    context={}
    return render(request,"app/Quick_Links.html",context)

def Gallery(request):
    context={}
    return render(request,"app/Gallery.html",context)

def Contact_Us(request):
    context={}
    return render(request,"app/Contact_Us.html",context)

def Logins(request):
    context={}
    return render(request,"app/Logins.html",context)