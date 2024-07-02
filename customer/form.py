from django import forms
from customer.models import Customer, Diet_Plan_Package


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_person',
                  'age', 'date_of_birth',
                  'gender', 'contact_number',
                  'landmark', 'phone_number',
                  'address', 'social_number',
                  'city', 'email',
                  'state', 'website',
                  'country', 'note']
        widgets = {'name': forms.TextInput(attrs={'class': '  form-control', 'required': True, 'placeholder': 'name'}),
                   'contact_person': forms.TextInput(attrs={'class': '  form-control'}),
                   'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}),
                   'gender': forms.Select(attrs={'class': '  form-control'}),
                   'address': forms.TextInput(attrs={'class': '  form-control'}),
                   'landmark': forms.TextInput(attrs={'class': '  form-control'}),
                   'city': forms.TextInput(attrs={'class': ' form-control'}),
                   'state': forms.TextInput(attrs={'class': '  form-control'}),
                   'country': forms.TextInput(attrs={'class': '  form-control','value':'Nepal'}),
                   'contact_number': forms.TextInput(attrs={'class': ' form-control select_me','required': True,}),
                   'phone_number': forms.TextInput(attrs={'class': ' form-control select_me'}),
                   'social_number': forms.TextInput(attrs={'class': ' form-control'}),
                   'email': forms.TextInput(attrs={'class': '  form-control select_me'}),
                   'website': forms.TextInput(attrs={'class': ' form-control'}),
                   'note': forms.TextInput(attrs={'class': ' form-control'})}

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        contact_number = cleaned_data.get("contact_number")
        instance = self.instance

        if Customer.objects.filter(name=name, contact_number=contact_number).exclude(pk=instance.pk).exists():
            raise forms.ValidationError("A customer with this name and contact number already exists.")

        return cleaned_data


class PackageForm(forms.ModelForm):
    class Meta:
        model = Diet_Plan_Package
        fields = ['package_name',
                  'package_cost',

                  'package_service',
                  'package_validity_time',
                  'package_validity',
                  'package_visibility', ]
        widgets = {'package_name': forms.TextInput(attrs={'class': '  form-control'}),
                   'package_cost': forms.NumberInput(attrs={'class': '  form-control'}),
                   'package_service': forms.TextInput(attrs={'class': 'form-control'}),
                   'package_visibility': forms.CheckboxInput(attrs={'class': 'form-control'}),
                   'package_validity': forms.CheckboxInput(attrs={'class': '  form-control'}),
                   'package_validity_time': forms.NumberInput(attrs={'class': '  form-control'}),
                   }

    def clean(self):
        cleaned_data = super().clean()
        package_name = cleaned_data.get("package_name")
        instance = self.instance

        if Diet_Plan_Package.objects.filter(package_name=package_name).exclude(pk=instance.pk).exists():
            raise forms.ValidationError("A Package with this name already exists.")

        return cleaned_data
