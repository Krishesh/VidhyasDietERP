from django.shortcuts import render, redirect

from customer.models import Customer, Customer_Stats
from inquiry.models import Inquiry, Customer_Family_Disease


# Create your views here.
def inquiry_list(request):
    context = {
        'inquiry': Inquiry.objects.all().filter(trash=False)
    }
    return render(request, 'inquiry/inquiry_list.html', context)


def add_inquiry_form(request):
    return render(request, 'inquiry/add_inquiry.html')


def edit_inquiry_form(request):
    context = {
        'inquiry': Inquiry.objects.get(id=request.GET.get('id'))
    }
    return render(request, 'inquiry/edit_inquiry.html', context)


def add_inquiry(request):
    if request.method == 'POST':
        # create customer First
        customer = Customer()
        customer.name = request.POST.get('customer_name')
        customer.age = request.POST.get('customer_age')
        customer.gender = request.POST.get('customer_gender')
        customer.profession = request.POST.get('customer_profession')
        customer.contact_number = request.POST.get('customer_contact_number')
        customer.social_number = request.POST.get('customer_social_number')
        customer.address = request.POST.get('customer_address')
        customer.email = request.POST.get('customer_email')
        customer.annual_income = request.POST.get('customer_annual_income')
        customer.save()

        # customer stats
        customer_Stats = Customer_Stats()
        from datetime import date
        customer_Stats.customer = customer
        customer_Stats.entry_date = date.today()
        weight = request.POST.get('customer_weight')
        height = request.POST.get('customer_height')
        waist = request.POST.get('customer_waist')
        hip = request.POST.get('customer_hip')
        customer_Stats.weight = weight
        customer_Stats.height = height
        customer_Stats.waist = waist
        customer_Stats.hip = hip

        bmi = float(weight) / ((float(height)/100) * (float(height)/100))
        whr = float(waist) / float(hip)
        print('bmi' + str(bmi))
        print('whr' + str(whr))
        customer_Stats.bmi = round(bmi, 2)
        customer_Stats.whr = round(whr, 2)
        customer_Stats.save()

        # inquiry Data

        inquiry = Inquiry()
        inquiry.customer_name = customer
        inquiry.customer_health_state = request.POST.get('customer_health_state')
        inquiry.customer_any_prescription = request.POST.get('customer_any_prescription')
        inquiry.customer_had_full_body_check_up = request.POST.get('customer_had_full_body_check_up')
        inquiry.customer_any_prescription = request.POST.get('customer_any_prescription')
        print(request.POST.getlist('customer_suffered_any_disease[]'))
        inquiry.customer_suffered_any_disease = request.POST.getlist('customer_suffered_any_disease[]pagal')
        inquiry.customer_thought_about_workout = request.POST.get('customer_thought_about_workout')
        inquiry.customer_activity_level = request.POST.get('customer_activity_level')
        inquiry.customer_any_symptoms = request.POST.get('customer_any_symptoms')
        inquiry.customer_lifestyle = request.POST.get('customer_lifestyle')
        inquiry.note = request.POST.get('note')
        inquiry.save()

        disease = request.POST.getlist('disease[]')
        relation = request.POST.getlist('relation[]')
        age = request.POST.getlist('age[]')
        disease_note = request.POST.getlist('disease_note[]')
        for i in range(len(disease)):
            customer_Family_Disease = Customer_Family_Disease()
            customer_Family_Disease.disease = disease[i]
            customer_Family_Disease.relation = relation[i]
            customer_Family_Disease.age = age[i]
            customer_Family_Disease.disease_note = disease_note[i]

            customer_Family_Disease.save()
            inquiry.customer_family_disease.add(customer_Family_Disease)

    return redirect("/inquiry_list")


def edit_inquiry(request):
    if request.method == 'POST':
        # create customer First
        customer = Customer()
        customer.name = request.POST.get('customer_name')
        customer.age = request.POST.get('customer_age')
        customer.gender = request.POST.get('customer_gender')
        customer.profession = request.POST.get('customer_profession')
        customer.contact_number = request.POST.get('customer_contact_number')
        customer.social_number = request.POST.get('customer_social_number')
        customer.address = request.POST.get('customer_address')
        customer.email = request.POST.get('customer_email')
        customer.annual_income = request.POST.get('customer_annual_income')
        customer.save()

        # customer stats
        customer_Stats = Customer_Stats()
        from datetime import date
        customer_Stats.customer = customer
        customer_Stats.entry_date = date.today()
        weight = request.POST.get('customer_weight')
        height = request.POST.get('customer_height')
        waist = request.POST.get('customer_waist')
        hip = request.POST.get('customer_hip')
        customer_Stats.weight = weight
        customer_Stats.height = height
        customer_Stats.waist = waist
        customer_Stats.hip = hip

        bmi = float(weight) / (float(height) * float(height))
        whr = float(waist) / float(hip)
        print('bmi' + bmi)
        print('whr' + whr)
        customer_Stats.bmi = bmi
        customer_Stats.whr = whr

        customer_Stats.save()

        # inquiry Data

        inquiry = Inquiry()
        inquiry.customer_name = customer
        inquiry.customer_health_state = request.POST.get('customer_health_state')
        inquiry.customer_any_prescription = request.POST.get('customer_any_prescription')
        inquiry.customer_had_full_body_check_up = request.POST.get('customer_had_full_body_check_up')
        inquiry.customer_any_prescription = request.POST.get('customer_any_prescription')
        inquiry.customer_suffered_any_disease = request.POST.get('customer_suffered_any_disease')
        inquiry.customer_thought_about_workout = request.POST.get('customer_thought_about_workout')
        inquiry.customer_activity_level = request.POST.get('customer_activity_level')
        inquiry.customer_any_symptoms = request.POST.get('customer_any_symptoms')
        inquiry.note = request.POST.get('note')
        inquiry.save()

        disease = request.POST.getlist('disease[]')
        relation = request.POST.getlist('relation[]')
        age = request.POST.getlist('age[]')
        disease_note = request.POST.getlist('disease_note[]')
        for i in range(len(disease)):
            customer_Family_Disease = Customer_Family_Disease()
            customer_Family_Disease.disease = disease[i]
            customer_Family_Disease.relation = relation[i]
            customer_Family_Disease.age = age[i]
            customer_Family_Disease.disease_note = disease_note[i]

            customer_Family_Disease.save()
            inquiry.customer_family_disease.add(customer_Family_Disease)

    return redirect("/inquiry_list")


def trash_inquiry(request):
    inquiry_id = request.POST.get('trash_id')
    inquiry = Inquiry.objects.get(id=inquiry_id)
    inquiry.trash = True
    inquiry.save()
    return redirect("/inquiry_list")


def details_inquiry(request):
    inquiry = Inquiry.objects.get(id=request.GET.get('id'))
    context = {
        'inquiry': inquiry,
        'customer_stats': Customer_Stats.objects.filter(customer=inquiry.customer_name)
    }
    return render(request, 'inquiry/details_inquiry.html', context)
