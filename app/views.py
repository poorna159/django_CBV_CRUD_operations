from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *


from django.urls import reverse_lazy


# List view displaying all objects(this is static url suffix) 
class SchoolList(ListView):
    model=School
    context_object_name='allSO'

#Detail View displaying selected object(school)Details
class School_Detail(DetailView):
    model=School
    context_object_name='DOSI'
    template_name='app\School_Detail.html'

#Create View displaying without instance(new)form for inserting
class SchoolCreate(CreateView):
    model=School
    fields='__all__'

#Update View displaying wit instance form for updateing 
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

#Delete View deleting the specified object school 
class SchoolDelete(DeleteView):
    model=School
    context_object_name='dso'
    success_url=reverse_lazy('SchoolList')
