from django.shortcuts import render, redirect

from account.models import Account
from customer.models import Diet_Plan_Package, Customer
from humanresource.models import Employee
from inquiry.models import Inquiry
from registration.models import Registration

from constance import config


# Create your views here.
def registration_list(request):
    context = {
        'registration': Registration.objects.all().filter(trash=False).order_by('registration_date')
    }
    return render(request, 'registration/registration_list.html', context)


def registration_print(request, registration_id):
    context = {
        'registration': Registration.objects.get(id=registration_id)
    }
    return render(request, 'registration/registration_print.html', context)


def inquiry_to_registration_form(request):
    print(config)
    context = {
        'inquiry': Inquiry.objects.get(id=request.GET.get('id')),
        'diet_plan': Diet_Plan_Package.objects.all(),
        'employee': Employee.objects.all(),
        'config': config
    }
    return render(request, 'registration/inquiry_to_registration.html', context)


def inquiry_to_registration(request):
    if request.method == 'POST':
        registration = Registration()

        from datetime import date
        registration.registration_date = date.today()

        registration.client_status = 'Registered'
        registration.registration_status = 'CREATED'
        inquiry = Inquiry.objects.get(id=request.POST.get('inquiry_id'))

        customer = inquiry.customer_name
        package_booked = Diet_Plan_Package.objects.get(id=request.POST.get('package_booked_select'))
        customer.name = request.POST.get('customer_name')
        customer.gender = request.POST.get('customer_gender')
        customer.date_of_birth = request.POST.get('customer_date_of_birth')
        customer.contact_number = request.POST.get('customer_contact_number')
        customer.social_number = request.POST.get('customer_social_number')
        customer.address = request.POST.get('customer_address')
        customer.diet_plan = package_booked
        customer.save()

        inquiry.inquiry_status = "Registered"
        inquiry.save()

        registration.customer = customer
        registration.employee = request.user.profile.employee
        registration.account_by = Employee.objects.get(id=request.POST.get('account_by'))
        registration.inquiry = inquiry

        registration.discount_amount = request.POST.get('discount')
        registration.total_amount = request.POST.get('total_amount')

        registration.received_amount = request.POST.get('received_amount')
        registration.due_amount = request.POST.get('due_amount')
        registration.receipt_bill_no = request.POST.get('bill_number')

        registration.package_booked = request.POST.get('package_booked')
        registration.package_cost = request.POST.get('package_cost')
        registration.package_service = request.POST.get('package_service')
        registration.therapy_package_start = request.POST.get('therapy_package_start')
        registration.therapy_package_end = request.POST.get('therapy_package_end')
        registration.gym_package_start = request.POST.get('gym_package_start')
        registration.gym_package_end = request.POST.get('gym_package_end')

        registration.save()
        registration.registration_id = str(inquiry.inquiry_id) + '-' + str(registration.pk) + 'R'
        registration.save()

        account = Account()
        account.account_created_by = Employee.objects.get(id=request.POST.get('account_by'))
        account.client = customer
        account.create_by = request.user

        account.discount = request.POST.get('discount')
        account.total_amount = request.POST.get('total_amount')
        account.received_amount = request.POST.get('received_amount')
        account.due_amount = request.POST.get('due_amount')
        account.receipt_bill_no = request.POST.get('bill_number')
        account.account_reference = registration.registration_id
        account.save()
        return redirect('/registration_list/')


def trash_registration(request):
    registration_id = request.POST.get('registration_id')
    registration = Registration.objects.get(id=registration_id)
    registration.trash = True
    registration.save()
    return redirect("/registration_list")


def edit_registration_form(request):
    context = {
        'registration': Registration.objects.get(id=request.GET.get('id')),
        'diet_plan': Diet_Plan_Package.objects.all(),
        'employee': Employee.objects.all()
    }
    return render(request, 'registration/edit_registration.html', context)


def edit_registration(request):
    if request.method == 'POST':
        registration = Registration.objects.get(id=request.GET.get('id'))

        from datetime import date
        registration.registration_date = date.today()

        registration.registration_status = 'EDITED'

        registration.account_by = Employee.objects.get(id=request.POST.get('account_by'))

        registration.total_amount = request.POST.get('package_cost')
        registration.received_amount = request.POST.get('received_amount')
        registration.due_amount = request.POST.get('due_amount')
        registration.receipt_bill_no = request.POST.get('bill_number')

        registration.package_booked = request.POST.get('package_booked')
        registration.package_cost = request.POST.get('package_cost')
        registration.package_service = request.POST.get('package_service')
        registration.therapy_package_start = request.POST.get('therapy_package_start')
        registration.therapy_package_end = request.POST.get('therapy_package_end')
        registration.gym_package_start = request.POST.get('gym_package_start')
        registration.gym_package_end = request.POST.get('gym_package_end')

        registration.save()
        return redirect('/registration_list/')


def registration_to_rebook_form(request):
    context = {
        'registration': Registration.objects.get(id=request.GET.get('id')),
        'diet_plan': Diet_Plan_Package.objects.all(),
        'employee': Employee.objects.all(),
        'config': config
    }
    return render(request, 'registration/registration_to_rebook.html', context)


def registration_to_rebook(request):
    if request.method == 'POST':
        old_registration = Registration.objects.get(id=request.GET.get('id'))
        registration = Registration()

        from datetime import date
        registration.registration_date = date.today()

        registration.client_status = 'Re-Booked'
        registration.registration_status = 'CREATED'
        customer = Customer.objects.get(id=old_registration.customer.id)

        package_booked = Diet_Plan_Package.objects.get(id=request.POST.get('package_booked_select'))

        customer.diet_plan = package_booked
        customer.save()

        registration.customer = customer
        registration.employee = request.user.profile.employee
        registration.account_by = Employee.objects.get(id=request.POST.get('account_by'))
        registration.inquiry = old_registration.inquiry

        registration.discount_amount = request.POST.get('discount')
        registration.total_amount = request.POST.get('total_amount')

        registration.received_amount = request.POST.get('received_amount')
        registration.due_amount = request.POST.get('due_amount')
        registration.receipt_bill_no = request.POST.get('bill_number')

        registration.package_booked = request.POST.get('package_booked')
        registration.package_cost = request.POST.get('package_cost')
        registration.package_service = request.POST.get('package_service')
        registration.therapy_package_start = request.POST.get('therapy_package_start')
        registration.therapy_package_end = request.POST.get('therapy_package_end')
        registration.gym_package_start = request.POST.get('gym_package_start')
        registration.gym_package_end = request.POST.get('gym_package_end')

        registration.registration_id = old_registration.registration_id + '-RB'
        registration.save()

        account = Account()
        account.account_created_by = Employee.objects.get(id=request.POST.get('account_by'))
        account.client = customer
        account.create_by = request.user

        account.discount = request.POST.get('discount')
        account.total_amount = request.POST.get('total_amount')
        account.received_amount = request.POST.get('received_amount')
        account.due_amount = request.POST.get('due_amount')
        account.receipt_bill_no = request.POST.get('bill_number')
        account.account_reference = registration.registration_id
        account.save()

        return redirect('/registration_list/')
