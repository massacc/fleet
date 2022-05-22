from django.urls import path, include
from . import views



app_name = 'vehicle'

urlpatterns = [
    path('', views.vehicle_filter, name='vehicles'),
    path('vehicle/<int:pk>', views.edit, name = 'edit'),
    path('create/', views.create, name='create'),
    path('delete-confirm/<str:vehicle_ids>', views.delete_confirm, name='delete_confirm'),
    path('accounts/', include('django.contrib.auth.urls')),
]
