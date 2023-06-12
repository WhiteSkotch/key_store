from django import forms

class AddMoneyForm(forms.Form):
    amount = forms.DecimalField(max_digits=15, decimal_places=2)