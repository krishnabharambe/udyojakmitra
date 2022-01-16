import re
from django.shortcuts import redirect, render

from app.models import IndiPageContent, appDocuments as M_appDocuments, Advertisements as M_Advertisements, Schemes as M_Schemes, Collaborations as M_Collaborations

# rootUrl = "http://127.0.0.1:8000"
rootUrl = "http://udyojakmitra.org"
# Create your views here.
def Backindex(request):
    return render(request, 'backapp/index.html')

def AdminAboutUs(request):
    IPC = IndiPageContent.objects.filter(page="AboutUs").first()
    if request.method == 'POST':
        if IPC:
            IPC.page = "AboutUs"
            IPC.pageContent = request.POST['pageContent']
            IPC.save()
            return redirect('AdminAboutUs')
        else:
            IPCAdd = IndiPageContent()
            IPCAdd.page = "AboutUs"
            IPCAdd.pageContent = request.POST['pageContent']
            IPCAdd.save()
            return redirect('AdminAboutUs')
    else:
        return render(request, 'backapp/Pages/AdminAboutUs.html',{'IPC':IPC})



def appDocuments(request):
    ADocuments = M_appDocuments.objects.all()
    if request.method == 'POST':
        if 'deleteDocument' in request.POST:
            mad = M_appDocuments.objects.get(id=request.POST['docid'])
            mad.delete()
            return redirect('appDocuments')
        elif 'addDocument' in request.POST:
            ad = M_appDocuments()
            ad.title = request.POST['title']
            ad.document4 = request.FILES['myfile']
            ad.save()
            return redirect('appDocuments')
        else:
            return redirect('appDocuments')
    else:
        return render(request, 'backapp/Pages/appDocuments.html',{'ADocuments':ADocuments,"rootUrl":rootUrl})


def appSchemes(request):
    ASchemes = M_Schemes.objects.all()
    if request.method == "POST":
        if 'addScheme' in request.POST:
            msa = M_Schemes()
            msa.title = request.POST['title']
            msa.image = request.FILES['image']
            msa.pageContent = request.POST['pageContent']
            if 'document4' in request.FILES:
                msa.document4 = request.FILES['document4']
            msa.save()
            return redirect('appSchemes')
        if 'EditScheme' in request.POST:
            ms = M_Schemes.objects.get(id=request.POST['schemeID'])
            ms.title = request.POST['title']
            ms.pageContent = request.POST['pageContent']
            if 'image' in request.FILES:
                ms.image = request.FILES['image']
            if 'document4' in request.FILES:
                ms.document4 =request.FILES['document4']
            ms.save()
            return redirect('appSchemes')
        if 'deleteScheme' in request.POST:
            ms = M_Schemes.objects.get(id=request.POST['schemeID'])
            ms.delete()
            return redirect('appSchemes')

    else:
        return render(request, 'backapp/Pages/appSchemes.html',{"rootUrl":rootUrl,'ASchemes':ASchemes})


def appAdvertisements(request):
    AAdvertisements = M_Advertisements.objects.all()
    if request.method == "POST":
        if 'addAdvertisement' in request.POST:
            msa = M_Advertisements()
            msa.title = request.POST['title']
            msa.image = request.FILES['image']
            msa.pageContent = request.POST['pageContent']
            if 'document4' in request.FILES:
                msa.document4 = request.FILES['document4']
            msa.save()
            return redirect('appAdvertisements')
        if 'EditAdvertisement' in request.POST:
            ms = M_Advertisements.objects.get(id=request.POST['AdvertisementID'])
            ms.title = request.POST['title']
            ms.pageContent = request.POST['pageContent']
            if 'image' in request.FILES:
                ms.image = request.FILES['image']
            if 'document4' in request.FILES:
                ms.document4 =request.FILES['document4']
            ms.save()
            return redirect('appAdvertisements')
        if 'deleteAdvertisement' in request.POST:
            ms = M_Advertisements.objects.get(id=request.POST['AdvertisementID'])
            ms.delete()
            return redirect('appAdvertisements')

    else:
        return render(request, 'backapp/Pages/appAdvertisements.html',{"rootUrl":rootUrl,'AAdvertisements':AAdvertisements})


def Collaborations(request):
    MCBL = M_Collaborations.objects.all()
    if request.method == 'POST':
        if 'addCollaboration' in request.POST:
            cbl = M_Collaborations()
            cbl.image = request.FILES['image']
            cbl.name = request.POST['name']
            cbl.pageContent = request.POST['pageContent']
            cbl.save()
            return redirect('Collaborations')
        elif 'editCollaboration' in request.POST:
            mcbl = M_Collaborations.objects.get(id=request.POST['cblid'])
            if 'image' in request.FILES:
                mcbl.image = request.FILES['image']
            mcbl.name = request.POST['name']
            mcbl.pageContent = request.POST['pageContent']
            mcbl.save()
            return redirect('Collaborations')
        elif 'deleteCollaboration' in request.POST:
            mcbl = M_Collaborations.objects.get(id=request.POST['cblid'])
            mcbl.delete()
            return redirect('Collaborations')
        else:
            return redirect('Collaborations')
    else:
        return render(request, 'backapp/Pages/Collaborations.html',{'MCBL':MCBL, "rootUrl":rootUrl})