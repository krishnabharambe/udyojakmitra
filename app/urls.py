from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('About_Us/',views.About_Us,name='About_Us'),
    path('Regional_List/',views.Regional_List,name='Regional_List'),
    path('Documents/',views.Documents,name='Documents'),
    path('Advertisements/',views.Advertisements,name='Advertisements'),
    path('Advertisements/<id>',views.IndexAdvertisements,name='IndexAdvertisements'),
    path('Schemes/',views.Schemes,name='Schemes'),
    path('Schemes/<id>',views.IndexSchemes,name='IndexSchemes'),
    path('Quick_Links/',views.Quick_Links,name='Quick_Links'),
    path('Gallery/',views.Gallery,name='Gallery'),
    path('Contact_Us/',views.Contact_Us,name='Contact_Us'),
    path('Logins/',views.Logins,name='Logins'),
    path('CustomersReg/',views.CustomersReg,name='CustomersReg'),
    path('WorkerReg/',views.WorkerReg,name='WorkerReg'),
]
