from django.contrib import admin

from app.models import ImageSlider, IndiPageContent, appDocuments, Schemes,Advertisements

# Register your models here.
admin.site.register(ImageSlider)
admin.site.register(IndiPageContent)
admin.site.register(appDocuments)
admin.site.register(Schemes)
admin.site.register(Advertisements)