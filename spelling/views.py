from django.shortcuts import render
from django.views import generic
from .models import Tub

# Create your views here.

class IndexView(generic.ListView):
    template_name = "spelling/index.html"
    context_object_name = "a_queryset"
    
    def get_queryset(self):
        queryset = Tub.objects.none()
        return queryset
