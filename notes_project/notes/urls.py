from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('new/', views.note_create, name='note_create'),
]