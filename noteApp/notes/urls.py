from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notes),
    path('insert_note/', views.insert_notes, name='insert_notes'),
]