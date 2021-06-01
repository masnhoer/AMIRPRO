from django.shortcuts import render

from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'amir/amir_dashboard.html'


class Mfilist(TemplateView):
    template_name = 'amir/mfi-list.html'