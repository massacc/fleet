from django.urls import path, include
from . import views



app_name = 'vehicles'

urlpatterns = [
    path('vehicle/<int:vehicle_id>/registration-add', views.registration_create, name='reg_add'),
    path('vehicle/<int:pk>', views.edit, name = 'edit'),
    path('vehicle/list', views.ListVehicles.as_view(), name='plate-list'),
    path('create/', views.create, name='create'),
    path('delete-confirm/<str:vehicle_ids>', views.delete_confirm, name='delete_confirm'),
    path('registrations/<int:vehicle_id>', views.registrations_list, name='registrations'),
    path('', views.vehicle_filter, name='vehicles'),
]
