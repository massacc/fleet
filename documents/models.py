from django.db import models
#from django.forms import FileField
from django.utils.translation import gettext_lazy as _
from vehicles.models import Vehicle
from django.shortcuts import reverse

class Document(models.Model):
    vehicle = models.ManyToManyField(
        Vehicle, 
        blank = True,
        related_name = 'vehicle',
        verbose_name = _('Vehicle')
    )
    file = models.FileField(
        null = True,
        blank = True,
        verbose_name = _('File')
    )

    title = models.CharField(
        max_length = 50,
        verbose_name = _('title'),
        null = True,
        blank = True,
    )

    description = models.TextField(
        null = True,
        blank = True,
        verbose_name = _('description')
    )

    created = models.DateField(
        auto_now_add = True,
        verbose_name = _('Created')
    )
    updated = models.DateField(
        auto_now = True,
        verbose_name = _('Updated')
    )

    def __str__(self):
        if self.vehicle.all():
            return f'{self.title} - ({self.vehicle})'
        else:
            return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('documents:edit',
                        args = [self.pk])