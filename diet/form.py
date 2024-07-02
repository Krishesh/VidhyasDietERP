from django import forms
from django.contrib.auth.models import User

from customer.models import Customer_Stats
from diet.models import LogBook, BodyComposition


class LogBookForm(forms.ModelForm):
    class Meta:
        model = LogBook
        fields = ['client', 'create_by', 'after_weight', 'before_weight', 'activity', 'treatment_type']

        widgets = {
            'client': forms.Select(attrs={'class': 'form-control select2 ', 'required': True}),
            'create_by': forms.Select(attrs={'class': 'form-control'}),
            'before_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'after_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'activity': forms.TextInput(attrs={'class': '  form-control'}),
            'treatment_type': forms.TextInput(attrs={'class': '  form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(LogBookForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['create_by'].queryset = User.objects.filter(id=user.id)


class BMIForm(forms.ModelForm):
    class Meta:
        model = BodyComposition
        fields = ['client', 'create_by', 'muscle_mass', 'fat_percentage',
                  'weight',
                  'bone_density',
                  'bmi',
                  'body_water',
                  'bmr']

        widgets = {
            'client': forms.Select(attrs={'class': 'form-control select2 ', 'required': True}),
            'create_by': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'muscle_mass': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'bone_density': forms.NumberInput(attrs={'class': '  form-control'}),
            'bmi': forms.NumberInput(attrs={'class': '  form-control'}),
            'body_water': forms.NumberInput(attrs={'class': '  form-control'}),
            'bmr': forms.NumberInput(attrs={'class': '  form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BMIForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['create_by'].queryset = User.objects.filter(id=user.id)

