from django.contrib import admin
from .models import Doctor, DocumentImage, LegalInformation, ServiceCategory, Service, ServiceImage, Contact
from solo.admin import SingletonModelAdmin

admin.site.register(ServiceCategory)
admin.site.register(Doctor)
admin.site.register(ServiceImage)
admin.site.register(DocumentImage)
admin.site.register(LegalInformation)
admin.site.register(Contact, SingletonModelAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)