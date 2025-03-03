from django.forms import ModelForm
from django import forms
from .models import Property, Property_Unit, Lease_Agreement

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        exclude =["property_id"]
        widgets = {
            'tags':forms.CheckboxSelectMultiple()
        }

        def __init__(self, *args, **kwargs):
            super(PropertyForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})


class PropertyUnitForm(ModelForm):
    class Meta:
        model= Property_Unit
        field="__all__"
        exclude = ["unit_id"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

        def __init__(self, *args, **kwargs):
            super(PropertyUnitForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})


class LeaseAgreementForm(ModelForm):
    class Meta:
        model= Lease_Agreement
        field= "__all__"
        exclude = ["agreement_id"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

        def __init__(self, *args, **kwargs):
            super(LeaseAgreementForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})