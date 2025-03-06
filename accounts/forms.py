from django import forms
from .models import User


class LandlordUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'address', 'company_name', 'contact_information']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(LandlordUserForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user

class TenantUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'address', 'lease_start_date', 'lease_end_date', 'lease_document']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(TenantUserForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user

class TenantOnboardingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['lease_start_date', 'lease_end_date', 'lease_document']