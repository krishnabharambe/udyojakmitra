from django.contrib import admin

from app.models import ImageSlider, IndiPageContent, appDocuments, Schemes,Advertisements,StateIND, District, Taluka, CityVillage, Worker, Customers

from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(ImageSlider)
admin.site.register(IndiPageContent)
admin.site.register(appDocuments)
admin.site.register(Schemes)
admin.site.register(Advertisements)
admin.site.register(Worker)
admin.site.register(Customers)


@admin.register(StateIND)
class StateINDAdmin(ImportExportModelAdmin):
    pass

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    pass

@admin.register(Taluka)
class TalukaAdmin(ImportExportModelAdmin):
    pass

@admin.register(CityVillage)
class CityVillageAdmin(ImportExportModelAdmin):
    pass
