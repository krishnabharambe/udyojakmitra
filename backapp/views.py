from django.shortcuts import redirect, render

from app.models import IndiPageContent, appDocuments as M_appDocuments, Advertisements as M_Advertisements, Schemes as M_Schemes

rootUrl = "http://127.0.0.1:8000"
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
            return redirect(appSchemes)
    else:
        return render(request, 'backapp/Pages/appSchemes.html',{"rootUrl":rootUrl})
    