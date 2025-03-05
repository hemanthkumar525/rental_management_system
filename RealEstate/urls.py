from django.urls import path
from . import views

urlpatterns= [
    path('', views.property_view, name='real_estate'),
    path('property_create/', views.property_create, name = "property_create"),
    path('property_unit_create/', views.property_unit_create, name = "property_unit_create"),
    path('lease_create/', views.lease_agreement_create, name='lease_create'),

    path('property_edit/<int:pk>/',views.property_edit, name="property_edit"),
    path('property_unit_edit/<int:pk>/', views.property_unit_edit, name = "property_unit_edit"),
    path('lease_edit/<int:pk>/', views.lease_agreement_edit, name="lease_edit"),
    
    path('property_delete/<int:pk>/', views.property_delete, name="property_delete"),
    path('property_unit_delete/<int:pk>/', views.property_unit_delete, name="property_unit_delete"),
    path('lease_delete/<int:pk>/', views.lease_agreement_delete, name= "lease_delete"),
]