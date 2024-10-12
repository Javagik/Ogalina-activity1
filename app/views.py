from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/About.html'

class ContactPageView(TemplateView):
    template_name = 'app/Contact.html'
