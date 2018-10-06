from django.shortcuts import render
from . import models
# Create your views here.
from django.views.generic import ListView,DetailView,TemplateView

class Index(TemplateView):
    template_name = 'index.html'

class List(ListView):
    template_name = 'list.html'
    model = models.School

class Detail(DetailView):
    context_object_name = 'school_detail'
    template_name = 'detail.html'
    model = models.School