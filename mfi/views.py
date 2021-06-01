from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class MFIDashboard(TemplateView):
    template_name = 'mfi/mfidashboard.html'

class Entryform(TemplateView):
    template_name = 'mfi/mfientryform.html'