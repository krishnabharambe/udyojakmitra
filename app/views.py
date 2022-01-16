from django.shortcuts import redirect, render, resolve_url
from .models import BusinessOwner, DistrictHandler, ImageSlider, IndiPageContent, M_Operator, TalukaHandler, WorkerLoan, appDocuments as M_appDocuments, Advertisements as M_Advertisements, Schemes as M_Schemes, StateIND, District, Taluka, CityVillage, Worker, Customers, Collaborations, HomeImage
# Create your views here.
rootUrl = "http://127.0.0.1:8000"

StateINDInst = StateIND.objects.filter(Status="Active")
DistrictInst = District.objects.filter(Status="Active")
TalukaInst = Taluka.objects.filter(Status="Active")
CityVillageInst = CityVillage.objects.filter(Status="Active")

def index(request):
    IS = ImageSlider.objects.all()
    msa = M_Advertisements.objects.all()
    cbl = Collaborations.objects.all()
    mSchemes = M_Schemes.objects.all()
    HI = HomeImage.objects.all().first()
    context = {'IS': IS, 'index': 'index','msa':msa,'cbl':cbl,'mgsa':mSchemes, 'HI':HI}
    return render(request, "app/index.html", context)

def About_Us(request):
    IPC = IndiPageContent.objects.filter(page="AboutUs").first()
    context = {'IPC': IPC, 'About_Us': 'About_Us'}
    return render(request, "app/About_Us.html", context)


def Regional_List(request):
    context = {}
    return render(request, "app/Regional_List.html", context)


def Documents(request):
    ADocuments = M_appDocuments.objects.all()
    context = {'ADocuments': ADocuments,
               "rootUrl": rootUrl, 'Documents': 'Documents'}
    return render(request, "app/Documents.html", context)


def IndexAdvertisements(request, id):
    ms = M_Advertisements.objects.get(id=id)
    return render(request, 'app/PageView.html', {"rootUrl": rootUrl, 'ms': ms, 'Advertisements': 'Advertisements'})


def Advertisements(request):
    msa = M_Advertisements.objects.all()
    context = {'msa': msa, 'rootUrl': rootUrl,
               'Advertisements': 'Advertisements'}
    return render(request, "app/Advertisements.html", context)


def IndexSchemes(request, id):
    ms = M_Schemes.objects.get(id=id)
    return render(request, 'app/PageView.html', {"rootUrl": rootUrl, 'ms': ms, 'Schemes': 'Schemes'})


def Schemes(request):
    mSchemes = M_Schemes.objects.all()
    context = {'Schemes': 'Schemes', 'msa': mSchemes, 'rootUrl': rootUrl}
    return render(request, "app/Schemes.html", context)


def Quick_Links(request):
    context = {}
    return render(request, "app/Quick_Links.html", context)


def Gallery(request):
    context = {}
    return render(request, "app/Gallery.html", context)


def Contact_Us(request):
    context = {}
    return render(request, "app/Contact_Us.html", context)


def Logins(request):
    context = {}
    return render(request, "app/Logins.html", context)


def CustomersReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = Customers()
        cvs.fullname = request.POST['fullname']
        cvs.address = request.POST['address']
        cvs.contact = request.POST['contact']
        cvs.Gender = request.POST['Gender']
        cvs.DOB = request.POST['DOB']
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/Customers.html", context)


def WorkerReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = Worker()
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.fullname = request.POST['fullname']
        cvs.BusinessName = request.POST['BusinessName']
        cvs.WorkType = request.POST['WorkType']
        cvs.AadharNo = request.POST['AadharNo']
        cvs.PanNo = request.POST['PanNo']
        cvs.Contact = request.POST['Contact']
        cvs.email = "black"
        cvs.Address = request.POST['Address']
        cvs.accountHolderName = request.POST['accountHolderName']
        cvs.accountNo = request.POST['accountNo']
        cvs.IFSC_Code = request.POST['IFSC_Code']
        cvs.IFSC_Branch = request.POST['IFSC_Branch']
        cvs.Ans1 = request.POST['Ans1']
        cvs.Ans2 = request.POST['Ans2']
        cvs.Ans3 = request.POST['Ans3']
        cvs.Ans4 = request.POST['Ans4']
        cvs.Ans5 = request.POST['Ans5']
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/Worker.html", context)



def WorkerLoanReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = WorkerLoan()
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.fullname = request.POST['fullname']
        cvs.BusinessName = request.POST['BusinessName']
        cvs.WorkType = request.POST['WorkType']
        cvs.AadharNo = request.POST['AadharNo']
        cvs.PanNo = request.POST['PanNo']
        cvs.Contact = request.POST['Contact']
        cvs.email = "black"
        cvs.Address = request.POST['Address']
        cvs.accountHolderName = request.POST['accountHolderName']
        cvs.accountNo = request.POST['accountNo']
        cvs.IFSC_Code = request.POST['IFSC_Code']
        cvs.IFSC_Branch = request.POST['IFSC_Branch']
        cvs.Ans1 = request.POST['Ans1']
        cvs.Ans2 = request.POST['Ans2']
        cvs.Ans3 = request.POST['Ans3']
        cvs.Ans4 = request.POST['Ans4']
        cvs.Ans5 = request.POST['Ans5']
        cvs.Ans6 = request.POST['Ans6']
        cvs.Ans7 = request.POST['Ans7']
        cvs.Ans8 = request.POST['Ans8']
        cvs.Ans9 = request.POST['Ans9']
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/WorkerLoan.html", context)


def BusinessOwnerReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = BusinessOwner()
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.fullname = request.POST['fullname']
        cvs.BusinessName = request.POST['BusinessName']
        cvs.WorkType = request.POST['WorkType']
        cvs.AadharNo = request.POST['AadharNo']
        cvs.PanNo = request.POST['PanNo']
        cvs.Contact = request.POST['Contact']
        cvs.email = "black"
        cvs.Address = request.POST['Address']
        cvs.accountHolderName = request.POST['accountHolderName']
        cvs.accountNo = request.POST['accountNo']
        cvs.IFSC_Code = request.POST['IFSC_Code']
        cvs.IFSC_Branch = request.POST['IFSC_Branch']
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/BusinessOwnerReg.html", context)


def DistrictHandlerReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = DistrictHandler()
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.fullname = request.POST['fullname']
        cvs.AadharNo = request.POST['AadharNo']
        cvs.PanNo = request.POST['PanNo']
        cvs.Contact = request.POST['Contact']
        cvs.email = "black"
        cvs.Address = request.POST['Address']
        cvs.profilepic = request.FILES['profilepic']
        cvs.accountHolderName = request.POST['accountHolderName']
        cvs.accountNo = request.POST['accountNo']
        cvs.IFSC_Code = request.POST['IFSC_Code']
        cvs.IFSC_Branch = request.POST['IFSC_Branch']
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/DistrictHandler.html", context)



def TalukaHandlerReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = TalukaHandler()
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.fullname = request.POST['fullname']
        cvs.AadharNo = request.POST['AadharNo']
        cvs.PanNo = request.POST['PanNo']
        cvs.Contact = request.POST['Contact']
        cvs.email = "black"
        cvs.Address = request.POST['Address']
        cvs.profilepic = request.FILES['profilepic']
        cvs.accountHolderName = request.POST['accountHolderName']
        cvs.accountNo = request.POST['accountNo']
        cvs.IFSC_Code = request.POST['IFSC_Code']
        cvs.IFSC_Branch = request.POST['IFSC_Branch']
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/TalukaHandler.html", context)


def OperatorReg(request):
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst}

    if request.method=='POST':
        cvs = M_Operator()
        cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
        cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
        cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
        cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
        cvs.fullname = request.POST['fullname']
        cvs.AadharNo = request.POST['AadharNo']
        cvs.PanNo = request.POST['PanNo']
        cvs.Contact = request.POST['Contact']
        cvs.email = "black"
        cvs.Address = request.POST['Address']
        cvs.profilepic = request.FILES['profilepic']
        cvs.accountHolderName = request.POST['accountHolderName']
        cvs.accountNo = request.POST['accountNo']
        cvs.IFSC_Code = request.POST['IFSC_Code']
        cvs.IFSC_Branch = request.POST['IFSC_Branch']
        cvs.save()
        return redirect('index')
    else:
        return render(request, "app/Operator.html", context)






