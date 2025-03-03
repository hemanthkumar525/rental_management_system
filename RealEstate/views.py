from django.shortcuts import render
from django.http import HttpResponse
from .forms import PropertyForm, PropertyUnitForm, LeaseAgreementForm


def property_view(request):
    property_create_form = PropertyForm()
    if request.method == 'POST':
        property_create_form = PropertyForm(request.POST, request.FILES)
        if property_create_form.is_valid():
            property_create_form.save()
            return HttpResponse("Property Created Successfully")
    context = {"property_form": property_create_form}
   
    return render(request, 'RealEstate/property.html', context)

def property_unit_view(request):
    property_unit_create_form = PropertyUnitForm()

    if request.method == 'POST':
        property_unit_create_form = PropertyUnitForm(request.POST, request.FILES)
        if property_unit_create_form.is_valid():
            property_unit_create_form.save()
            return HttpResponse("Property Unit Created Successfully")
    context = {"property_unit_form": property_unit_create_form}

    return render(request, 'RealEstate/property_unit.html', context)

def lease_agreement_view(request):
    lease_agreement_view_form = LeaseAgreementForm()
    if request.method == 'POST':
        lease_agreement_view_form = LeaseAgreementForm(request.POST, request.FILES)
        if lease_agreement_view_form .is_valid():
            lease_agreement_view_form .save()
            return HttpResponse("Property Unit Created Successfully")
    context = {"lease_form":lease_agreement_view_form}

    return render(request, 'RealEstate/lease.html', context)
