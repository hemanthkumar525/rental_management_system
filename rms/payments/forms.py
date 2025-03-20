from django import forms
from .models import UserPayment
class UserPaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount (USD)")
