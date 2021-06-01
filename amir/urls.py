from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path('mfi', views.Mfilist.as_view(), name='mfi'),
]
