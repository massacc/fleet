from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Entity(models.Model):
    
    created = models.DateField(auto_now_add=True, null=True, verbose_name=_('Date of creation'))
    updated = models.DateField(auto_now=True, verbose_name=_('Last modified'))
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, unique=True, null=True, verbose_name=_('Name'))
    short_name = models.CharField(max_length=250, unique=True, null=True, verbose_name=_('Short name'))
    #first_name = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('First name'))
    #last_name = models.CharField(max_length=250, verbose_name=_('Last name'))
    nip = models.CharField(max_length=25, unique=True, blank=True, null=True, verbose_name=_('Tax number'))
    vies = models.CharField(max_length=25, unique=True, blank=True, null=True, verbose_name=_('Vies number')) 
    regon = models.CharField(max_length=25, unique=True, blank=True, null=True, verbose_name=_('Regon number'))
    pesel = models.CharField(max_length=25, unique=True, blank=True, null=True, verbose_name=_('PESEL number'))
    vat_payer = models.BooleanField()
    remarks = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Remarks'))
    type = models.CharField(max_length=3, blank=True, null=True, verbose_name=_('Type')) 
    
    class Meta:
        abstract = True

class Address(models.Model):
    created = models.DateField(auto_now_add=True,null=True, verbose_name=_('Date of creation'))
    updated = models.DateField(auto_now=True, verbose_name=_('Last modified'))
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    
    #entity = models.ForeignKey(Entity, null=True, blank=False, related_name='adresses', on_delete=models.CASCADE)
    city = models.CharField(max_length=250, verbose_name=_('City / town'))
    street = models.CharField(max_length=250, verbose_name=_('Street'))
    number = models.CharField(max_length=25, verbose_name=_('House number'))
    flat = models.CharField(max_length=25, verbose_name=_('Flat number'))
    postal_code = models.CharField(max_length=25, verbose_name=_('Zip code'))
    country_code = models.CharField(max_length=3, verbose_name=_('Country code'))
    region = models.CharField(max_length=250, verbose_name=_('Region'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        abstract = True
#konto INTEGER, - tylko w customer 
#waluta TEXT,
#znacznik TEXT,

