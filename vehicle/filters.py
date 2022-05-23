import django_filters
from .models import Vehicle
from django.utils.translation import gettext_lazy as _

class VehicleFilter(django_filters.FilterSet):
    plate= django_filters.CharFilter(
                                field_name='registrations__plate',
                                lookup_expr='icontains',
                                label= _('Registration plates'))
    year_gte = django_filters.NumberFilter(
                               field_name = 'production_year',
                               lookup_expr='gte',
                               label= _('Production year from:'))
    year_lte = django_filters.NumberFilter(
                                field_name='production_year',
                                lookup_expr='lte',
                                label= _('to'))
    make = django_filters.CharFilter(
                                field_name='name__make__make',
                                lookup_expr='icontains',
                                label= _('Make'))
    vehicle_model = django_filters.CharFilter(
                                field_name='name_name',
                                lookup_expr='icontains',
                                label='Model')



    class Meta:
        model = Vehicle
        #fields = {
         #       'registration__plate':['icontains'],
          #      'production_year':['lt', 'gt']
         #}
        #fields = {
        #        'name__make__make':['icontains']
        #}
        fields = ['plate', 'year_gte', 'year_lte', 'make', 'vehicle_model']
