from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name',
                  'contact_person',
                  'age',
                  'date_of_birth',
                  'gender',
                  'address',
                  'city',
                  'state',
                  'country',
                  'contact_number',
                  'phone_number',
                  'social_number',
                  'email',
                  'website',
                  'note']
        widgets = {'name': forms.TextInput(attrs={'class': '  form-control'}),
                   'contact_person': forms.TextInput(attrs={'class': '  form-control'}),
                   'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}),
                   'gender': forms.Select(attrs={'class': '  form-control'}),
                   'address': forms.TextInput(attrs={'class': '  form-control'}),
                   'city': forms.TextInput(attrs={'class': ' form-control'}),
                   'state': forms.TextInput(attrs={'class': '  form-control'}),
                   'country': forms.TextInput(attrs={'class': '  form-control'}),
                   'contact_number': forms.TextInput(attrs={'class': ' form-control select_me'}),
                   'phone_number': forms.TextInput(attrs={'class': ' form-control select_me'}),
                   'social_number': forms.TextInput(attrs={'class': ' form-control'}),
                   'email': forms.TextInput(attrs={'class': '  form-control select_me'}),
                   'website': forms.TextInput(attrs={'class': ' form-control'}),
                   'note': forms.TextInput(attrs={'class': ' form-control'})}

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        contact_number = cleaned_data.get("contact_number")

        if Customer.objects.filter(name=name, contact_number=contact_number).exists():
            raise forms.ValidationError("A customer with this name and contact number already exists.")

        return cleaned_data
