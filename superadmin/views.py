from django.shortcuts import render
from django.contrib.auth.models import User

def property_owners_list(request):
    property_owners = User.objects.filter(groups__name="property_owner")
    return render(request, "superadmin.html", {"property_owners": property_owners})
