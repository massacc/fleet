from django.urls import path, include
from . import views



app_name = 'vehicle'

urlpatterns = [
    path('', views.vehicle_filter, name='vehicles'),
    path('details/<int:pk>', views.vehicle_detail, name = 'details'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.vehicle_edit, name='vehicle_edit'),
    path('delete-confirm/<str:vehicle_ids>', views.delete_confirm, name='delete_confirm'),
    path('accounts/', include('django.contrib.auth.urls')),
]
