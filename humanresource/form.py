from django import forms
from customer.models import Customer
from humanresource.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', ]
        widgets = {'name': forms.TextInput(attrs={'class': '  form-control'})}

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")

        if Department.objects.filter(name=name).exists():
            raise forms.ValidationError("A Department with this name already exists.")

        return cleaned_data
