from django import forms
from django.contrib.auth.models import User

from customer.models import Customer_Stats, Customer
from diet.models import LogBook, BodyComposition, DietPlan


class LogBookForm(forms.ModelForm):
    class Meta:
        model = LogBook
        fields = ['client', 'create_by', 'after_weight', 'before_weight', 'activity', 'treatment_type']

        widgets = {
            'create_by': forms.Select(attrs={'class': 'form-control'}),
            'before_weight': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'after_weight': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'activity': forms.TextInput(attrs={'class': '  form-control'}),
            'treatment_type': forms.TextInput(attrs={'class': '  form-control'}),
        }
    client = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(LogBookForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['create_by'].queryset = User.objects.filter(id=user.id)
        self.fields['client'].queryset = Customer.objects.all()
        self.fields['client'].label_from_instance = lambda obj: f'{obj.name} - {obj.contact_number}'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control select2'


class BMIForm(forms.ModelForm):
    class Meta:
        model = BodyComposition
        fields = ['client', 'create_by', 'muscle_mass', 'fat_percentage',
                  'weight',
                  'bone_density',
                  'bmi',
                  'protein',
                  'total_intake_calories',
                  'body_water',
                  'bmr']

        widgets = {
            'create_by': forms.Select(attrs={'class': 'form-control', 'required': True}, ),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'muscle_mass': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'fat_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'bone_density': forms.NumberInput(attrs={'class': '  form-control', 'step': 'any'}),
            'bmi': forms.NumberInput(attrs={'class': '  form-control', 'step': 'any'}),
            'body_water': forms.NumberInput(attrs={'class': '  form-control', 'step': 'any'}),
            'total_intake_calories': forms.NumberInput(attrs={'class': '  form-control', 'step': 'any'}),
            'protein': forms.NumberInput(attrs={'class': '  form-control', 'step': 'any'}),
            'bmr': forms.NumberInput(attrs={'class': '  form-control', 'step': 'any'}),
        }

    client = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BMIForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['create_by'].queryset = User.objects.filter(id=user.id)

        self.fields['client'].queryset = Customer.objects.all()
        self.fields['client'].label_from_instance = lambda obj: f'{obj.name} - {obj.contact_number}'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control select2'


class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = '__all__'
        widgets = {
            'created_by': forms.Select(
                attrs={'class': 'form-control select2', 'label': 'Created By', 'required': True}),
            'day': forms.Select(attrs={'class': 'form-control select2', 'label': 'Day'}),

            'cereals_pulses': forms.TextInput(attrs={'class': 'form-control'}),
            'vegetables': forms.TextInput(attrs={'class': 'form-control'}),
            'fruits': forms.TextInput(attrs={'class': 'form-control'}),
            'meat_eggs': forms.TextInput(attrs={'class': 'form-control'}),
            'milk_products': forms.TextInput(attrs={'class': 'form-control'}),
            'fat_oil_products': forms.TextInput(attrs={'class': 'form-control'}),

            'breakfast_time': forms.TextInput(attrs={'class': 'form-control'}),
            'breakfast_chapatti_select': forms.Select(attrs={'class': 'form-control'}),
            'breakfast_chapatti': forms.TextInput(attrs={'class': 'form-control'}),
            'breakfast_dry_bread': forms.TextInput(attrs={'class': 'form-control'}),
            'breakfast_oats_cereals': forms.TextInput(attrs={'class': 'form-control'}),
            'breakfast_egg': forms.TextInput(attrs={'class': 'form-control'}),
            'breakfast_vegetables': forms.TextInput(attrs={'class': 'form-control'}),

            'mid_morning_snack_time': forms.TextInput(attrs={'class': 'form-control'}),
            'mid_morning_fruits': forms.TextInput(attrs={'class': 'form-control'}),
            'mid_morning_yogurt_select': forms.Select(attrs={'class': 'form-control'}),
            'mid_morning_yogurt': forms.TextInput(attrs={'class': 'form-control'}),

            'lunch_time': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_roti': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_rice_select': forms.Select(attrs={'class': 'form-control'}),
            'lunch_rice': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_lentils': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_vegetable_curry': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_leafy_vegetables': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_meat_select': forms.Select(attrs={'class': 'form-control'}),
            'lunch_meat_tofu': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_fish': forms.TextInput(attrs={'class': 'form-control'}),

            'afternoon_snack_time': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon_snack_sandwich': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon_snack_bread_roll': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon_snack_beaten_rice': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon_snack_roasted_corn': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon_snack_pulses': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon_snack_raw_vegetables': forms.TextInput(attrs={'class': 'form-control'}),

            'dinner_time': forms.TextInput(attrs={'class': 'form-control'}),
            'dinner_rice_dhindo_select': forms.Select(attrs={'class': 'form-control'}),
            'dinner_rice_dhindo': forms.TextInput(attrs={'class': 'form-control'}),
            'dinner_dry_bread': forms.TextInput(attrs={'class': 'form-control'}),
            'dinner_lentils': forms.TextInput(attrs={'class': 'form-control'}),
            'dinner_vegetables': forms.TextInput(attrs={'class': 'form-control'}),

            'carbohydrates_calories': forms.TextInput(attrs={'class': 'form-control'}),
            'carbohydrates_grams': forms.TextInput(attrs={'class': 'form-control'}),
            'proteins_calories': forms.TextInput(attrs={'class': 'form-control'}),
            'proteins_grams': forms.TextInput(attrs={'class': 'form-control'}),
            'fat_calories': forms.TextInput(attrs={'class': 'form-control'}),
            'fat_grams': forms.TextInput(attrs={'class': 'form-control'}),
            'total_calories': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_level': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),

        }

    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DietPlanForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['created_by'].queryset = User.objects.filter(id=user.id)
        self.fields['customer'].queryset = Customer.objects.all()
        self.fields['customer'].label_from_instance = lambda obj: f'{obj.name} - {obj.contact_number}'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['customer'].widget.attrs['class'] = 'form-control select2'
