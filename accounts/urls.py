from django.urls import path
from . import views
from RealEstate import urls

app_name = 'accounts'

urlpatterns = [
    path('', views.users_list, name="users_list"),
    # Tenant Management (Super Admin)
    path('tenant_create/', views.tenant_create, name='tenant_create'),
    path('tenant_update/<str:pk>/', views.tenant_update, name='tenant_update'),
    path('tenant_delete/<str:pk>/', views.tenant_delete, name='tenant_delete'),

    # Landlord Management (Super Admin)
    path('landlord_create/', views.landlord_create, name='landlord_create'),
    path('landlord_update/<str:pk>/', views.landlord_update, name='landlord_update'),
    path('landlord_delete/<str:pk>/', views.landlord_delete, name='landlord_delete'),

    # Site Configuration (Super Admin)
    path('siteconfig/', views.site_config, name='site_config'),

]