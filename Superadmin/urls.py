from django.urls import path
from .views import *

app_name = 'Superadmin'

urlpatterns = [
    path('', home, name="home"),
    path("add_property_owner/", add_property_owner, name="add_property_owner"),
]