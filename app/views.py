from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from app.models import *



class SchoolList(ListView):
    model=School
    context_object_name='allSO'


class School_Detail(DetailView):
    model=School
    context_object_name='DOSI'
    template_name='app\School_Detail.html'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


