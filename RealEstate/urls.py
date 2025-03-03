from django.urls import path
from . import views

urlpatterns= [
    path('', views.property_view, name='real_estate'),
    path('property_unit/', views.property_unit_view, name = "property_unit"),
    path('lease_agreement/', views.lease_agreement_view, name='lease_agreement')
]