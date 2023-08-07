from django.shortcuts import render

# Create your views here.



from django.views.generic import ListView
from app.models import *


# List view displaying all objects(this is static url suffix) 

class SchoolList(ListView):
    model=School
    context_object_name='allSO'

