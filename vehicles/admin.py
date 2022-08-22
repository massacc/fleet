from django.contrib import admin
from .models import Vehicle, Company, Manufacturer, Ownership, VehicleModel, Registration
# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Company)
admin.site.register(Vehicle)
admin.site.register(Ownership)
admin.site.register(VehicleModel)
admin.site.register(Registration)
