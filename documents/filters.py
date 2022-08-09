import django_filters
#from django.db import models
from .models import Document
from django.utils.translation import gettext_lazy as _

class DocumentFilter(django_filters.FilterSet):
    vehicle = django_filters.CharFilter(
                                field_name='vehicle__active_plate',
                                lookup_expr='icontains',
                                label= _('Registration plates'))
    '''
    year_gte = django_filters.NumberFilter(
                               field_name = 'production_year',
                               lookup_expr='gte',
                               label= _('Production year from:'))
    year_lte = django_filters.NumberFilter(
                                field_name='production_year',
                                lookup_expr='lte',
                                label= _('to'))
    '''
    title = django_filters.CharFilter(
                                field_name='title',
                                lookup_expr='icontains',
                                label= _('Title'))
    description = django_filters.CharFilter(
                                field_name='description',
                                lookup_expr='icontains',
                                label='Description')



    class Meta:
        model = Document
        #fields = {
         #       'registration__plate':['icontains'],
          #      'production_year':['lt', 'gt']
         #}
        #fields = {
        #        'name__make__make':['icontains']
        #}
        fields = ['vehicle', 'title', 'description']