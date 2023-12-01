from django.db import models
from entities.models import Entity, Address
from django.utils.translation import gettext_lazy as _


class Company(Entity):
    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        
class CompanyAddress(Address):
    
    entity = models.ForeignKey(Company, null=True, blank=False, related_name='adresses', on_delete=models.CASCADE)
