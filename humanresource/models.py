from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=100, blank=True, null=True, default='')

    # basic info
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    date_of_birth = models.CharField(max_length=100, blank=True, default='', null=True,
                                     verbose_name='Date of birth (Y-M-D) ', )
    blood_group = models.CharField(max_length=100, blank=True, null=True, default='')
    nationality = models.CharField(max_length=100, blank=True, null=True, default='')
    c_gender = (('Male', 'Male'),
                ('Female', 'Female'),
                ('Other', 'Other'),
                ('', 'Default'))
    gender = models.CharField(choices=c_gender, max_length=15, null=True, default='', blank=True)
    c_marital = (('Single', 'Single'),
                 ('Married', 'Married'),
                 ('Legal Cohabitant', 'Legal Cohabitant'),
                 ('Widower', 'Widower'),
                 ('Divorced', 'Divorced'),
                 ('', 'Default'))
    marital = models.CharField(choices=c_marital, max_length=30, null=True, default='', blank=True)
    citizen_number = models.CharField(max_length=100, blank=True, null=True, default='')
    pan_number = models.CharField(max_length=100, blank=True, null=True, default='')

    employee_note = models.CharField(max_length=256, blank=True, null=True, default='')

    # contact Info
    address = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.CharField(max_length=100, blank=True, null=True, default='')
    contact = models.CharField(max_length=100, blank=True, null=True, default='')
    work_phone_number = models.CharField(max_length=100, null=True, blank=True, default='')
    work_email = models.CharField(max_length=100, blank=True, null=True, default='')

    # Guardian info
    guardian_name = models.CharField(max_length=100, blank=True, null=True, default='')
    guardian_relation = models.CharField(max_length=100, blank=True, null=True, default='')
    guardian_address = models.CharField(max_length=100, blank=True, null=True, default='')
    guardian_phone_number = models.CharField(max_length=100, blank=True, null=True, default='')

    # job responsibility
    job_position = models.CharField(max_length=30, blank=True, null=True, default='')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    fired = models.BooleanField(default=False)
    join_date = models.DateField(auto_created=True, auto_now_add=False, auto_now=False, null=True)
    left_date = models.DateField(auto_created=True, auto_now_add=False, auto_now=False, null=True, blank=True)
    branch = models.CharField(max_length=30, blank=True, null=True, default='')
    grade = models.CharField(max_length=30, blank=True, null=True, default='')
    ratings = models.CharField(max_length=30, blank=True, null=True, default='')

    # quarter benefits
    stay_in_quarters = models.BooleanField(default=False)

    employee_type = models.CharField(max_length=100, blank=True, null=True, default='')

    outsource_company = models.CharField(max_length=225, blank=True, null=True, default='')
    specialization = models.CharField(max_length=3000, blank=True, null=True, default='')
    terms_and_condition = models.CharField(max_length=3000, blank=True, null=True, default='')

    trashed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Salary(models.Model):
    # salary and payment info
    employee = models.OneToOneField(Employee, on_delete=models.DO_NOTHING)
    basic_salary = models.CharField(max_length=100, blank=True, default='')
    room_allowance = models.CharField(max_length=100, blank=True, default='')
    food_allowance = models.CharField(max_length=100, blank=True, default='')
    overtime_allowance = models.CharField(max_length=100, blank=True, default='')
    intensive = models.CharField(max_length=100, blank=True, default='')
    festival_bonus = models.CharField(max_length=100, blank=True, default='')
    other_allowance = models.CharField(max_length=100, blank=True, default='')
    provident_fund = models.CharField(max_length=100, blank=True, default='')

    # payment Info
    p_method = (('Cash', 'Cash'),
                ('Bank', 'Bank'),
                ('', 'Default'))
    payment_method = models.CharField(choices=p_method, max_length=100, blank=True, default='')

    # bank_details
    bank_name = models.CharField(max_length=100, blank=True, default='')
    bank_branch = models.CharField(max_length=100, blank=True, default='')
    bank_account_name = models.CharField(max_length=100, blank=True, default='')
    bank_account_number = models.CharField(max_length=100, blank=True, default='')

    # tax info
    tax_payer_employee = models.BooleanField(default=False)
    tax_rate = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.employee.name


class PlaySlip_Code(models.Model):
    ps_code = models.CharField(max_length=100, blank=True, default='')
    period_date = models.CharField(max_length=100, blank=True, default='')
    generated_date = models.CharField(max_length=100, blank=True, default='')
    created_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class Payslip(models.Model):
    # salary and payment info
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    payslip_code = models.ForeignKey(PlaySlip_Code, on_delete=models.DO_NOTHING)

    date = models.CharField(max_length=100, blank=True, default='')
    salary_period_from = models.CharField(max_length=100, blank=True, default='')
    salary_period_to = models.CharField(max_length=100, blank=True, default='')

    basic_salary = models.CharField(max_length=100, blank=True, default='')
    room_allowance = models.CharField(max_length=100, blank=True, default='')
    food_allowance = models.CharField(max_length=100, blank=True, default='')
    overtime = models.CharField(max_length=100, blank=True, default='')
    intensive = models.CharField(max_length=100, blank=True, default='')
    festival_bonus = models.CharField(max_length=100, blank=True, default='')
    other_allowance = models.CharField(max_length=100, blank=True, default='')
    provident_fund = models.CharField(max_length=100, blank=True, default='')
    total_salary = models.CharField(max_length=100, blank=True, default='')

    advance = models.CharField(max_length=100, blank=True, default='')
    provident_fund_deduction = models.CharField(max_length=100, blank=True, default='')
    room_benefit = models.CharField(max_length=100, blank=True, default='')
    social_security_tax = models.CharField(max_length=100, blank=True, default='')
    medical_loan_installment = models.CharField(max_length=100, blank=True, default='')
    leave_amount = models.CharField(max_length=100, blank=True, default='')
    total_deduction = models.CharField(max_length=100, blank=True, default='')

    net_salary_payable = models.CharField(max_length=100, blank=True, default='')

    payroll_type = models.CharField(max_length=100, blank=True, default='')
    verification_status = models.CharField(max_length=100, blank=True, default='')
    finished = models.BooleanField(default=False)
    stype = (('saved', 'saved'), ('submited', 'submited'), ('approved', 'approved'), ('canceled', 'canceled'))
    status = models.CharField(choices=stype, max_length=25, default='saved', blank=True)

    def __str__(self):
        return self.employee.name
