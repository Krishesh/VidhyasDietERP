from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from diet.form import LogBookForm, BMIForm
from diet.models import LogBook, BodyComposition

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
        'bodyComposition': BodyComposition.objects.all().order_by('recorded_at')  # To list all logbook entries if needed
    }
    return render(request, 'diet/body_composition/body_composition.html', context)

