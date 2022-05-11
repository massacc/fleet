from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import datetime

#coś tu napiszemy

class Company(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Manufacturer(models.Model):

    make = models.CharField(max_length = 250)

    def __str__(self):
        return f'{self.make}'


class VehicleModel(models.Model):

    VEHICLE_TYPES = [
        ('1', 'Lorry'),
        ('2','Truck-tractor'),
        ('3', 'Ballast tractor'),
        ('4', 'Trailer'),
        ('5', 'Semi-trailer'),
        ('6', 'Bus'),
        ('0', 'Other')]



    make = models.ForeignKey(Manufacturer,
                                on_delete=models.PROTECT,
                                related_name="vehicle_model")
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=10, choices=VEHICLE_TYPES)


    def __str__(self):
        return f'{self.make} {self.name}'

    class Meta:
        verbose_name = 'Vehicle model'
        verbose_name_plural = 'Vehicles models'

class Vehicle(models.Model):

    SUSPENSION_TYPES = [
        ('1', 'Air suspension'),
        ('2', 'Equivalent to air suspension'),
        ('3', 'Other')]

    name = models.ForeignKey(VehicleModel,
                                on_delete=models.PROTECT,
                                related_name = 'vehicle')

    first_registration = models.DateField(
                    help_text='Date of first registratrion in Poland')
    vin_number = models.CharField(max_length=50,
                        unique=True,
                        help_text='Chassis number / VIN / SN number')
    axles = models.IntegerField(
                                blank=True,
                                null=True,
                                verbose_name='Number of axles',
                                default=2)
    production_year = models.IntegerField(
                                validators=[MinValueValidator(1900)])
    weight = models.FloatField(
                            blank=True,
                            null=True,
                            verbose_name='Weight',
                            help_text='Vehicle weight (if semi-tractor)',
                            default=0)
    gvm = models.FloatField(
                        blank=True,
                        verbose_name='Gross vehicle mass',
                        help_text='Maximum permissible laden weight',
                        null=True,
                        default=0)
    gcwr = models.FloatField(
            blank=True,
            null=True,
            verbose_name = 'Gross combined weight rating',
            help_text =
            'maximum permissible laden weight of a vehicle combination',
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
        return reverse('vehicle:vehicle_detail',
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
                                    verbose_name='Registration date')
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

    class Meta:
       constraints = [UniqueConstraint(fields=['plate', 'start_date'], name='unuque_plate')]

