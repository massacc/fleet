from django.urls import path, include
from . import views



app_name = 'documents'

urlpatterns = [
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<str:ids>', views.delete, name='delete'),
    path('create/',views.create, name='create'),
    path('', views.doc_list, name='documents'),
]
