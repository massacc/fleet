from django.db import models
from django.db.models import UniqueConstraint
#from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from .validators import validate_future_date

class Company(models.Model):
    name = models.CharField(_('Name'),max_length=250)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):

    make = models.CharField(_('Make'), max_length = 250)

    def __str__(self):
        return f'{self.make}'

class VehicleModel(models.Model):

    VEHICLE_TYPES = [
        ('1', _('Lorry')),
        ('2', _('Truck-tractor')),
        ('3', _('Ballast tractor')),
        ('4', _('Trailer')),
        ('5', _('Semi-trailer')),
        ('6', _('Bus')),
        ('0', _('Other'))]
    make = models.ForeignKey(
                            Manufacturer,
                            on_delete = models.PROTECT,
                            related_name = "vehicle_model")
    name = models.CharField(_('Name'), max_length=250)
    type = models.CharField(
                    _('Type'),
                    max_length=10,
                    choices=VEHICLE_TYPES)

    def __str__(self):
        return f'{self.make} {self.name}'

    class Meta:
        verbose_name = 'Vehicle model'
        verbose_name_plural = 'Vehicle models'

class Vehicle(models.Model):

    SUSPENSION_TYPES = [
        ('1', _('Air suspension')),
        ('2', _('Equivalent to air suspension')),
        ('3', _('Other'))]

    name = models.ForeignKey(VehicleModel,
                                on_delete = models.PROTECT,
                                related_name = 'vehicle',
                                verbose_name = _('Name'))
    first_registration = models.DateField(
                    verbose_name = _('First registatrion'),
                    help_text = _('Date of first registratrion in Poland'))
    vin_number = models.CharField(
                    max_length = 50,
                    unique = True,
                    verbose_name = _('VIN'),
                    help_text = _('Chassis number / VIN / SN number'))
    axles = models.IntegerField(
                    blank = True,
                    null = True,
                    verbose_name = _('Number of axles'),
                    default = 2)
    production_year = models.IntegerField(
                                default=0)
    weight = models.FloatField(
                        blank = True,
                        null = True,
                        verbose_name = _('Weight'),
                        help_text = _('Vehicle weight (if semi-tractor)'),
                        default=0)
    gvm = models.FloatField(
                    blank = True,
                    verbose_name = _('Gross vehicle mass'),
                    help_text = _('Maximum permissible laden weight'),
                    null = True,
                    default = 0)
    gcwr = models.FloatField(
        blank = True,
        null = True,
        verbose_name = 'Gross combined weight rating',
        help_text =
            _('Maximum permissible laden weight of a vehicle combination'),
        default=0)

    suspension = models.CharField(max_length=10,
                                    choices= SUSPENSION_TYPES)


    @property
    def plate(self):
        #registration = Registration.objects.filter(id=self.id).order_by(
        #registration = self.registrations.order_by('-start_date')

        registration = self.registrations.filter(active=True)
        if registration:
            return f'{registration[0].plate}'
        else:
            return ''

    def __str__(self):
        if self.plate:
            return self.plate
        else:
            return f'{self.id}'

    def get_absolute_url(self):
        return reverse('vehicle:edit',
                        args = [self.pk])

class Ownership(models.Model):

    OWNERSHIP_TYPES = [
        ('0','Owner'),
        ('1','Co-owner - first named in the vehicle registration card'),
        ('2','Co-owner - second named in the vehicle registration card')
    ]

    vehicle = models.ForeignKey(Vehicle,
                        blank=True,
                        null=True,
                        on_delete=models.CASCADE,
                        related_name='ownerships')

    type = models.CharField(max_length=1,
                            choices=OWNERSHIP_TYPES,
                            default='0')

    percentage = models.IntegerField(
                                default=100,
                                verbose_name="Percentage of ownership")

    purchase_date = models.DateField(verbose_name = 'Purchase date')
    sell_date = models.DateField(verbose_name="Date of sell",
                                            blank=True)
    deregistration_date = models.DateField('Date of deregistration',
                                            blank=True)

    def __str__(self):
        return "Ownership " + str(self.id)

    class Meta:
        verbose_name = 'Ownership'
        verbose_name_plural = "Ownersphips"

class Registration(models.Model):

    vehicle = models.ForeignKey(Vehicle,
                        blank=True,
                        null=True,
                        on_delete=models.CASCADE,
                        related_name='registrations')

    start_date = models.DateField(blank=False,
                                    #default=datetime.now,
                                    null=True,
                                    verbose_name='Registration date',
                                    validators=[validate_future_date])
    end_date = models.DateField(blank=True,
                                    null=True,
                                    verbose_name='Deregistrarion date')
    plate = models.CharField(max_length=25,
                                verbose_name='Registration plate')

    created = models.DateField(verbose_name='Created',
                                auto_now_add=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.plate}'

    def get_absolute_url(self):
        return reverse('vehicle:',
                        args = [self.pk])
    class Meta:
       constraints = [UniqueConstraint(fields=['plate', 'start_date'], name='unuque_plate')]

