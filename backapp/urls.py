from django.urls import path
from . import views
urlpatterns = [
    path('',views.Backindex,name='Backindex'),
    path('Pages/About_Us',views.AdminAboutUs,name='AdminAboutUs'),
    path('Pages/appDocuments',views.appDocuments,name='appDocuments'),
    # path('Pages/appAdvertisements',views.appAdvertisements,name='appAdvertisements'),
    path('Pages/appSchemes',views.appSchemes,name='appSchemes'),
]

