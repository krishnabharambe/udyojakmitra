from django.contrib import admin

from app.models import BusinessOwner, DistrictHandler, ImageSlider, IndiPageContent, M_Operator, TalukaHandler, WorkerLoan, appDocuments, Schemes,Advertisements,StateIND, District, Taluka, CityVillage, Worker, Customers, Collaborations, HomeImage

from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(ImageSlider)
admin.site.register(IndiPageContent)
admin.site.register(appDocuments)
admin.site.register(Schemes)
admin.site.register(Advertisements)
admin.site.register(Worker)
admin.site.register(Customers)
admin.site.register(Collaborations)
admin.site.register(HomeImage)
admin.site.register(WorkerLoan)
admin.site.register(BusinessOwner)
admin.site.register(DistrictHandler)
admin.site.register(TalukaHandler)
admin.site.register(M_Operator)

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
