from django.http import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.contrib import messages
from .models import BusinessOwner, DistrictHandler, ImageSlider, IndiPageContent, M_Operator, TalukaHandler, WorkerLoan, appDocuments as M_appDocuments, Advertisements as M_Advertisements, Schemes as M_Schemes, StateIND, District, Taluka, CityVillage, Worker, Customers, Collaborations, HomeImage
# Create your views here.
# rootUrl = "http://127.0.0.1:8000"
rootUrl = "http://udyojakmitra.org"

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
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'IS': IS, 'index': 'index','msa':msa,'cbl':cbl,'mgsa':mSchemes, 'HI':HI, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/index.html", context)

def About_Us(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    IPC = IndiPageContent.objects.filter(page="AboutUs").first()
    context = {'IPC': IPC, 'About_Us': 'About_Us', 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/About_Us.html", context)


def Regional_List(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Regional_List.html", context)


def Documents(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ADocuments = M_appDocuments.objects.all()
    context = {'ADocuments': ADocuments,
               "rootUrl": rootUrl, 'Documents': 'Documents', 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Documents.html", context)


def IndexAdvertisements(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ms = M_Advertisements.objects.get(id=id)
    return render(request, 'app/PageView.html', {"rootUrl": rootUrl, 'ms': ms, 'Advertisements': 'Advertisements', 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})


def Advertisements(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    msa = M_Advertisements.objects.all()
    context = {'msa': msa, 'rootUrl': rootUrl,
               'Advertisements': 'Advertisements', 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Advertisements.html", context)


def IndexSchemes(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ms = M_Schemes.objects.get(id=id)
    return render(request, 'app/PageView.html', {"rootUrl": rootUrl, 'ms': ms, 'Schemes': 'Schemes', 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})


def Schemes(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    mSchemes = M_Schemes.objects.all()
    context = {'Schemes': 'Schemes', 'msa': mSchemes, 'rootUrl': rootUrl, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Schemes.html", context)


def Quick_Links(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Quick_Links.html", context)


def Gallery(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Gallery.html", context)


def Contact_Us(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Contact_Us.html", context)


def Logins(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
    return render(request, "app/Logins.html", context)


def CustomersReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}

    if request.method=='POST':
        if request.POST['pass_1'] == request.POST['pass_2']:
            cvsTest = Customers.objects.filter(email =request.POST['email'])
            if cvsTest :
                return redirect('CustomersRegFailure', email = request.POST['email'])
            else:
                cvs = Customers()
                cvs.fullname = request.POST['fullname']
                cvs.address = request.POST['address']
                cvs.contact = request.POST['contact']
                cvs.Gender = request.POST['Gender']
                cvs.DOB = request.POST['DOB']
                cvs.email = request.POST['email']
                cvs.password = request.POST['pass_2']
                cvs.StateID = StateIND.objects.get(id=request.POST['StateID'])
                cvs.DistrictID = District.objects.get(id=request.POST['DistrictID'])
                cvs.TalukaID = Taluka.objects.get(id=request.POST['TalukaID'])
                cvs.CityVillageID = CityVillage.objects.get(id=request.POST['CityVillageID'])
                cvs.save()
                return redirect('CustomersRegSuccess', id=cvs.id)
        else :
            messages.error(request,"Password doesn't match, Please try again")
            return redirect('CustomersReg')
    else:
        return render(request, "app/Customers.html", context)

def CustomersRegSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = Customers.objects.get(id=id)
    return render(request, "app/Success/CustomerRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})

def CustomersRegFailure(request, email):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    return render(request, "app/Success/CustomerRegF.html",{'email':email, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})

def WorkerReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}

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
        return redirect('WorkerRegSuccess', id=cvs.id)
    else:
        return render(request, "app/Worker.html", context)


def WorkerRegSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = Worker.objects.get(id=id)
    return render(request, "app/Success/WorkerRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})



def WorkerLoanReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}

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
        return redirect('WorkerLoanSuccess', id=cvs.id)
    else:
        return render(request, "app/WorkerLoan.html", context)


def WorkerLoanSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = WorkerLoan.objects.get(id=id)
    return render(request, "app/Success/WorkerLoanRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})

def BusinessOwnerReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}

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
        return redirect('BusinessOwnerRegSuccess', id=cvs.id)
    else:
        return render(request, "app/BusinessOwnerReg.html", context)

def BusinessOwnerRegSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = BusinessOwner.objects.get(id=id)
    return render(request, "app/Success/BusinessOwnerRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})


def DistrictHandlerReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}

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
        return redirect('DistrictHandlerRegSuccess', id=cvs.id)
    else:
        return render(request, "app/DistrictHandler.html", context)

def DistrictHandlerRegSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = DistrictHandler.objects.get(id=id)
    return render(request, "app/Success/DistrictHandlerRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})

def TalukaHandlerReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}

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
        return redirect('TalukaHandlerRegSuccess', id=cvs.id)
    else:
        return render(request, "app/TalukaHandler.html", context)

def TalukaHandlerRegSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = TalukaHandler.objects.get(id=id)
    return render(request, "app/Success/TalukaHandlerRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})

def OperatorReg(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    context = {'State': StateINDInst,
               'District': DistrictInst,
               'Taluka': TalukaInst,
               'CityVillage': CityVillageInst, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst}
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
        return redirect('OperatorRegSuccess', id=cvs.id)
    else:
        return render(request, "app/Operator.html", context)

def OperatorRegSuccess(request, id):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    ws = M_Operator.objects.get(id=id)
    return render(request, "app/Success/OperatorRegS.html",{'ws':ws, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})

def View_Login(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    if request.method == 'POST':
        if request.POST['LoginType'] == 'Customer_login':
            cust = Customers.objects.filter(email=request.POST['username'],password=request.POST['password'])
            if cust:
                request.session['login'] = request.POST['username']
                request.session['type'] = 'Customer_login'
                print("login - ",request.session['login'])
                print("type - ",request.session['type'])
                return redirect('index')
            else:
                pass
        elif request.POST['LoginType'] == 'Business_login':
            pass
        elif request.POST['LoginType'] == 'Operator_login':
            pass
        elif request.POST['LoginType'] == 'Worker_login':
            pass
        elif request.POST['LoginType'] == 'TalukaHandler_login':
            pass
        elif request.POST['LoginType'] == 'DistrictHandler_login':
            pass
        else :
            pass
    else:
        return render(request, "app/Login/Login.html",{'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})


def LogOut(request):
    try:
        del request.session['login']
        del request.session['type']
    except:
        pass
    return redirect('index')


def profile(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''

    if sessionTypeInst == 'Customer_login':
        cust = Customers.objects.filter(email=sessionInst).first()
    
    return render(request, 'app/Login/Profile.html',{'cust':cust, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})


def WorkersView(request):
    if request.session.has_key('login'):
        sessionInst = request.session['login']
    else:
        sessionInst = ''
    if request.session.has_key('type'):
        sessionTypeInst = request.session['type']
    else:
        sessionTypeInst=''
    wlist = Worker.objects.all()
    return render(request, 'app/WorkersView.html',{ 'wlist':wlist, 'sessionInst':sessionInst,'sessionTypeInst':sessionTypeInst})