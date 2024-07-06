from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from customer.models import Customer
from diet.form import LogBookForm, BMIForm, DietPlanForm
from diet.models import LogBook, BodyComposition, DietPlan

# views.py
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages


def create_logbook_and_stats(request, pk=None):
    if pk:
        logBook = get_object_or_404(LogBook, pk=pk)
    else:
        logBook = None

    if request.method == 'POST':
        if logBook:
            form = LogBookForm(request.POST, instance=logBook)
        else:
            form = LogBookForm(request.POST, user=request.user)

        if form.is_valid():
            logbook_instance = form.save()
            logbook_instance.create_or_update_customer_stats()  # Ensure customer stats are updated
            messages.success(request, 'LogBook entry saved successfully.')
            return redirect('diet:create_logbook_and_stats')  # Redirect to the form page after saving
    else:
        if logBook:
            form = LogBookForm(instance=logBook)
        else:
            form = LogBookForm(user=request.user)

    context = {
        'form': form,
        'logbook_entries': LogBook.objects.all().order_by('date')  # To list all logbook entries if needed
    }
    return render(request, 'diet/log_book/logbook.html', context)


def body_composition(request, pk=None):
    if pk:
        bodyComposition = get_object_or_404(BodyComposition, pk=pk)
    else:
        bodyComposition = None

    if request.method == 'POST':
        if bodyComposition:
            form = BMIForm(request.POST, instance=bodyComposition)
        else:
            form = BMIForm(request.POST, user=request.user)

        if form.is_valid():
            bodyComposition_instance = form.save()
            bodyComposition_instance.create_customer_stats()  # Ensure customer stats are updated
            messages.success(request, 'BMI  entry saved successfully.')
            return redirect('diet:bmi')  # Redirect to the form page after saving
    else:
        if bodyComposition:
            form = BMIForm(instance=bodyComposition)
        else:
            form = BMIForm(user=request.user)

    context = {
        'form': form,
        'bodyComposition': BodyComposition.objects.all().order_by('recorded_at')
        # To list all logbook entries if needed
    }
    return render(request, 'diet/body_composition/body_composition.html', context)


def create_diet_plan_new(request, customer_id_pk):
    customer = get_object_or_404(Customer, pk=customer_id_pk)

    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        if form.is_valid():
            diet_plan = form.save(commit=False)
            diet_plan.customer = customer
            diet_plan.created_by = request.user
            diet_plan.save()
            return redirect('customer:customer_detail', pk=customer_id_pk)
    else:
        form = DietPlanForm(initial={'customer': customer, 'created_by': request.user, 'created_date': timezone.now()})

    context = {
        'form': form,
        'customer': customer,
        'created_by': request.user,
        'created_date': timezone.now()
    }

    return render(request, 'diet/diet_plan/diet_plan_form.html', context)


def create_diet_plan(request):
    if request.method == 'POST':
        print(request.POST)
        form = DietPlanForm(request.POST, user=request.user)
        if form.is_valid():
            diet_plan = form.save(commit=False)
            diet_plan.created_by = request.user
            diet_plan.save()
            messages.success(request, 'Diet Plan created successfully.')
            return redirect('diet:diet_plan_list')
        else:
            print(form.errors)
    else:
        form = DietPlanForm(user=request.user)
    return render(request, 'diet/diet_plan/diet_plan_form.html', {'form': form})


def edit_diet_plan(request, pk):
    diet_plan = get_object_or_404(DietPlan, pk=pk)
    if request.method == 'POST':
        form = DietPlanForm(request.POST, instance=diet_plan, user=request.user)
        if form.is_valid():
            form.cleaned_data['customer'] = diet_plan.customer
            form.save()
            messages.success(request, 'Diet Plan updated successfully.')
            return redirect('diet:diet_plan_list')
        else:
            print(form.errors)
    else:
        form = DietPlanForm(instance=diet_plan, user=request.user)
    return render(request, 'diet/diet_plan/diet_plan_form.html', {'form': form})


def diet_plan_list(request):
    diet_plan = DietPlan.objects.order_by('created_date').filter(trashed=False)
    customer = Customer.objects.all()
    context = {
        'diet_plans': diet_plan,
        'customers': customer
    }
    return render(request, 'diet/diet_plan/diet_plan_list.html', context)


def diet_plan_print_nepali(request, pk):
    diet_plan = DietPlan.objects.get(id=pk)
    context = {
        'diet_plan': diet_plan,
    }
    return render(request, 'diet/diet_plan/vidhyas_diet_plan_nepali.html', context)


def diet_plan_print_english(request, pk):
    diet_plan = DietPlan.objects.get(id=pk)
    context = {
        'diet_plan': diet_plan,
    }
    return render(request, 'diet/diet_plan/vidhyas_diet_plan_english.html', context)


def diet_plan_trash(request):
    id = request.POST.get('trash_id')
    diet_plan = DietPlan.objects.get(id=id)
    diet_plan.trashed = True
    print('true')
    diet_plan.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def diet_plan_preview(request,pk):
    diet_plan = DietPlan.objects.get(id=pk)
    context = {
        'diet_plan': diet_plan,
    }
    return render(request, 'diet/diet_plan/vidhyas_diet_plan_preview.html', context)

