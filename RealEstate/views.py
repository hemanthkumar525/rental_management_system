from django.shortcuts import render
from django.http import HttpResponse
from .forms import PropertyForm, PropertyUnitForm, LeaseAgreementForm
from .models import Property, Property_Unit, Lease_Agreement

# List of all properties, property units and lease agreements
def property_view(request):
    properties = Property.objects.all()
    property_units = Property_Unit.objects.all()
    lease_agreements = Lease_Agreement.objects.all()
    context = {"properties": properties, "property_units": property_units, "lease_agreements": lease_agreements}
    return render (request, "RealEstate\property_list.html", context)

# Creating a new property
def property_create(request):
    property_form = PropertyForm()
    if request.method == 'POST':
        property_create_form = PropertyForm(request.POST, request.FILES)
        if property_create_form.is_valid():
            property_create_form.save()
            return HttpResponse("Property Created Successfully")
    context = {"property_form": property_form}
   
    return render(request, 'RealEstate/property.html', context)

# Creating a new property unit
def property_unit_create(request):
    property_unit_form = PropertyUnitForm()
    if request.method == 'POST':
        property_unit_form = PropertyUnitForm(request.POST, request.FILES)
        if property_unit_form.is_valid():
            property_unit_form.save()
            return HttpResponse("Property Unit Created Successfully")
    context = {"property_unit_form": property_unit_form}
    return render(request, 'RealEstate/property_unit.html', context)

# Create a new lease agreement
def lease_agreement_create(request):
    lease_agreement_form = LeaseAgreementForm()
    if request.method == 'POST':
        lease_agreement_view_form = LeaseAgreementForm(request.POST, request.FILES)
        if lease_agreement_view_form .is_valid():
            lease_agreement_view_form .save()
            return HttpResponse("Property Unit Created Successfully")
    context = {"lease_form":lease_agreement_form}
    return render(request, 'RealEstate/lease.html', context)


#  Edit a property
def property_edit(request, pk):
    property = Property.objects.get(id = pk)
    property_form = PropertyForm(instance = property)
    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES, instance = property)
        if property_form.is_valid():
            property_form.save()
            return HttpResponse("Property Updated Successfully")
    context = {"property_form":property_form}
    return render(request, "RealEstate\property.html", context)

# Edit a property unit
def property_unit_edit(request, pk):
    property_unit = Property_Unit.objects.get(id = pk)
    property_unit_form = PropertyUnitForm(instance = property_unit)
    if request.method == 'POST':
        property_unit_form = PropertyUnitForm(request.POST, request.FILES, instance = property_unit)
        if property_unit_form.is_valid():
            property_unit_form.save()
            return HttpResponse("Property Updated Successfully")
    context = {"property_unit_form":property_unit_form}
    return render(request, "RealEstate\property_unit.html", context)

# Edit a lease agreement
def lease_agreement_edit(request, pk):
    lease_agreement = Lease_Agreement.objects.get(id = pk)
    lease_agreement_form = LeaseAgreementForm(instance = lease_agreement)
    if request.method == "POST":
        lease_agreement_form = LeaseAgreementForm(request.POST, request.FILES, instance= lease_agreement)
        if lease_agreement_form.is_valid():
            lease_agreement_form.save()
            return HttpResponse("Lease Agreement Form Updated")
    context = {"lease_form": lease_agreement_form}
    return render(request, "RealEstate\lease.html", context)

# Delete a property
def property_delete(request, pk):
    property = Property.objects.get(id = pk)
    property.delete()
    return HttpResponse("Property Deleted Successfully")

# Delete a property unit
def property_unit_delete(request, pk):
    property_unit = Property_Unit.objects.get(id = pk)
    property_unit.delete()
    return HttpResponse("Property Unit Deleted Successfully")

# Delete a lease agreement
def lease_agreement_delete(request, pk):
    lease_agreement = Lease_Agreement.objects.get(id = pk)
    lease_agreement.delete()
    return HttpResponse("Lease Agreement Deleted Successfully")

