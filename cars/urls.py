from django.contrib import admin
from django.urls import path
from .views import CarListView,CarDetailView,CarCreateView,CarUpdateView,CarDeleteView 

urlpatterns = [
    
    path('',CarListView.as_view(),name='cars'),
    path('<int:pk>/',CarDetailView.as_view(),name='car_detail'),
    path('create/',CarCreateView.as_view(),name='car_create'),
    path('update/<int:pk>',CarUpdateView.as_view(),name='car_update'),
    path('delete/<int:pk>',CarDeleteView.as_view(),name='car_delete'),



]
