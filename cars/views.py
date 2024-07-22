from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from .models import Car
from django.urls import reverse_lazy

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'car_objects'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['model','brand','price']

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = "__all__"
    

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars')




   
