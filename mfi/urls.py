from django.urls import path

from . import views

urlpatterns = [
    path('mfidashboard', views.MFIDashboard.as_view(), name='mfidashboard'),
    path('mfientryform', views.Entryform.as_view(), name='mfientryform'),
]
