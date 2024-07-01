from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from humanresource.form import DepartmentForm
from humanresource.models import Department, Employee, Salary


# Create your views here.
def department_list(request, pk=None):
    if pk:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == 'POST':
        if department:
            form = DepartmentForm(request.POST, instance=department)
        else:
            form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('humanresource:department_list')
        else:
            print(form.errors)
    else:
        form = DepartmentForm(instance=department) if department else DepartmentForm()

    departments = Department.objects.all()
    return render(request, 'humanresource/department/department_list.html', {'form': form, 'departments': departments})


def delete_department(request):
    department = get_object_or_404(Department, pk=request.POST.get("trash_id"))
    department.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def employee_list(request):
    context = {
        'employee': Employee.objects.filter(trashed=False)
    }
    return render(request, 'humanresource/employee/employee_list.html', context)


def employee_details(request):
    post_id = request.GET.get('id')
    em = Employee.objects.get(id=post_id)
    join_date = str(em.join_date)
    try:
        salary = Salary.objects.get(employee=em)
    except Salary.DoesNotExist:
        salary = None

    context = {
        "employee": em,
        'department': Department.objects.all(),
        'salary': salary,
        'join_date': join_date,

    }
    return render(request, 'humanresource/employee/employee_details.html', context)


def add_employee_form(request):
    content = {
        'department': Department.objects.all()

    }
    return render(request, "humanresource/employee/add_employee.html", content)


def add_employee(request):
    if request.method == 'POST':
        employees = Employee()
        employees.branch = request.POST.get('branch')

        employees.department = Department.objects.get(name=request.POST.get('department'))

        # basic info
        employees.name = request.POST.get('name')
        employees.date_of_birth = request.POST.get('date_of_birth')
        employees.blood_group = request.POST.get('blood_group')
        employees.nationality = request.POST.get('nationality')
        employees.gender = request.POST.get('gender')
        employees.marital = request.POST.get('marital')
        employees.citizen_number = request.POST.get('citizen_number')
        employees.pan_number = request.POST.get('pan_number')
        employees.employee_type = request.POST.get('employee_type')
        employees.employee_note = request.POST.get('employee_note')

        # contact Info
        employees.address = request.POST.get('address')
        employees.email = request.POST.get('email')
        employees.contact = request.POST.get('contact')
        employees.work_phone_number = request.POST.get('work_phone_number')
        employees.work_email = request.POST.get('work_email')

        # Guardian info

        employees.guardian_name = request.POST.get('guardian_name')
        employees.guardian_relation = request.POST.get('guardian_relation')
        employees.guardian_address = request.POST.get('guardian_address')
        employees.guardian_phone_number = request.POST.get('guardian_phone_number')

        # job responsibility
        employees.job_position = request.POST.get('job_position')
        employees.join_date = request.POST.get('join_date')
        employees.grade = request.POST.get('grade')
        employees.ratings = request.POST.get('ratings')
        employees.stay_in_quarters = request.POST.get('stay_in_quarters')

        employees.save()
        employee_id = "EMP_" + str("%03d" % int(employees.id))
        employees.employee_id = employee_id
        employees.save()
        return redirect("humanresource:employee_list")

    else:
        return redirect("humanresource:employee_list")


def edit_employee_form(request):
    post_id = request.GET.get('id')
    em = Employee.objects.get(id=post_id)
    join_date = str(em.join_date)
    context = {
        "employee": Employee.objects.get(id=post_id),
        'department': Department.objects.all(),
        'join_date': join_date
    }
    return render(request, 'humanresource/employee/edit_employee.html', context)


def edit_employee(request):
    post_id = request.GET.get('id')
    employees = Employee.objects.get(id=post_id)

    if request.method == 'POST':

        employees.branch = request.POST.get('branch')
        employees.department = Department.objects.get(name=request.POST.get('department'))

        # basic info
        employees.name = request.POST.get('name')
        employees.date_of_birth = request.POST.get('date_of_birth')
        employees.blood_group = request.POST.get('blood_group')
        employees.nationality = request.POST.get('nationality')
        employees.gender = request.POST.get('gender')
        employees.marital = request.POST.get('marital')
        employees.citizen_number = request.POST.get('citizen_number')
        employees.pan_number = request.POST.get('pan_number')
        employees.employee_type = request.POST.get('employee_type')
        employees.employee_note = request.POST.get('employee_note')

        # contact Info
        employees.address = request.POST.get('address')
        employees.email = request.POST.get('email')
        employees.contact = request.POST.get('contact')
        employees.work_phone_number = request.POST.get('work_phone_number')
        employees.work_email = request.POST.get('work_email')

        # Guardian info

        employees.guardian_name = request.POST.get('guardian_name')
        employees.guardian_relation = request.POST.get('guardian_relation')
        employees.guardian_address = request.POST.get('guardian_address')
        employees.guardian_phone_number = request.POST.get('guardian_phone_number')

        # job responsibility
        employees.job_position = request.POST.get('job_position')
        employees.join_date = request.POST.get('join_date')
        employees.grade = request.POST.get('grade')
        employees.ratings = request.POST.get('ratings')

        employees.stay_in_quarters = request.POST.get('stay_in_quarters')

        employees.save()
        return redirect("humanresource:employee_list")

    else:
        return redirect("humanresource:employee_list")


def delete_employee(request):
    post_id = request.POST.get('trash_id')
    print(post_id)
    employees = Employee.objects.get(id=post_id)
    employees.trashed = True
    employees.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
