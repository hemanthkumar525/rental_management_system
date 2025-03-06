from django.urls import path
from . import views
from RealEstate import urls

app_name = 'accounts'

urlpatterns = [
    # User Management (Super Admin)
    path('user_create/', views.user_create, name='user_create'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_update/<int:pk>/', views.user_update, name='user_update'),
    path('user_delete/<int:pk>/', views.user_delete, name='user_delete'),

    # Tenant Management (Super Admin)
    path('tenant_create/', views.tenant_create, name='tenant_create'),
    path('tenant_list/', views.tenant_list, name='tenant_list'),
    path('tenant_update/<int:pk>/', views.tenant_update, name='tenant_update'),
    path('tenant_delete/<int:tenant_id>/', views.tenant_delete, name='tenant_delete'),

    # Landlord Management (Super Admin)
    path('landlord_create/', views.landlord_create, name='landlord_create'),
    path('landlord_list/', views.landlord_list, name='landlord_list'),
    path('landlord_update/<int:pk>/', views.landlord_update, name='landlord_update'),

    
    # Site Configuration (Super Admin)
    path('siteconfig/', views.site_config, name='site_config'),


    # Superadmin Dashboard
    path('superadmin_dashboard/', views.superadmin_dashboard, name='superadmin_dashboard'),
    
   
   

]