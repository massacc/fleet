from django.urls import path, include
from . import views



app_name = 'vehicles'

urlpatterns = [
    path('vehicle/<int:vehicle_id>/registration-add', views.registration_create, name='reg_add'),
    path('vehicle/<int:pk>', views.edit, name = 'edit'),
    path('create/', views.create, name='create'),
    path('delete-confirm/<str:vehicle_ids>', views.delete_confirm, name='delete_confirm'),
    path('', views.vehicle_filter, name='vehicles'),
]
