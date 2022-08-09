from django.urls import path, include
from . import views



app_name = 'documents'

urlpatterns = [
    path('edit/<int:id>', views.edit, name='edit'),
    path('create/',views.create, name='create'),
    path('', views.list, name='documents'),
]
