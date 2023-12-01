from django.contrib import admin

from .models import Company, CompanyAddress

class AddressInLine(admin.TabularInline):
    model = CompanyAddress

class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        AddressInLine,
    ]



admin.site.register(Company, CompanyAdmin)
