from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
def home(request):
    return render (request,"home.html")

def main(request):
    return render (request,"main.html")


class IndexView(TemplateView):
    template_name ='home.html'


