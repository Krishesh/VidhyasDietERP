from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect

from customer.form import CustomerForm, PackageForm
from customer.models import Diet_Plan_Package, Customer, Customer_Stats
from customer.serializers import Diet_Plan_Package_Serializer, Customer_Serializer
from diet.models import LogBook, DietPlan
from inquiry.models import Inquiry
from registration.models import Registration


# Create your views here.

def customer_list(request):
    context = {
        'customers': Customer.objects.filter(trashed=False),
    }
    return render(request, 'customer/customer_list.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    inquiry = Inquiry.objects.all().filter(customer_name=customer)
    print(Inquiry.objects.filter(customer_name__pk=customer.pk))
    context = {
        'customer': customer,
        'inquiry': inquiry,
        'customer_stats': Customer_Stats.objects.filter(customer=customer),
        'registration': Registration.objects.filter(customer=customer),
        'logbook_entries': LogBook.objects.filter(client=customer),
        'diet_plan': DietPlan.objects.filter(customer=customer)

    }
    return render(request, 'customer/customer_detail.html', context)


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
        else:
            # Handle the error
            print(form.errors)
    else:
        form = CustomerForm()
    return render(request, 'customer/add_customer.html', {'form': form})


def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
        else:
            # Handle the error
            print(form.errors)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/edit_customer.html', {'form': form, 'customer': customer})


def trash_customer(request):
    customer = get_object_or_404(Customer, pk=request.POST.get("trash_id"))
    customer.trashed = True
    customer.save()
    return redirect('customer:customer_list')


class DietPlanAPI(APIView):

    def get(self, request, format=None):
        notification = Diet_Plan_Package.objects.all()
        serializer = Diet_Plan_Package_Serializer(notification, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Diet_Plan_Package_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DietPlanDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Diet_Plan_Package.objects.get(pk=pk)
        except Diet_Plan_Package.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Diet_Plan_Package_Serializer(snippet)
        return Response(serializer.data)

    '''def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Diet_Plan_Package_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''


class CustomerAPI(APIView):

    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializer = Customer_Serializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Customer_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customer_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def vidhyas_package(request, pk=None):
    if pk:
        diet_Plan_Package = get_object_or_404(Diet_Plan_Package, pk=pk)
    else:
        diet_Plan_Package = None

    if request.method == 'POST':
        if diet_Plan_Package:
            form = PackageForm(request.POST, instance=diet_Plan_Package)
        else:
            form = PackageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer:vidhyas_package')
        else:
            print(form.errors)
    else:
        form = PackageForm(instance=diet_Plan_Package) if diet_Plan_Package else PackageForm()

    diet_Plan_Package = Diet_Plan_Package.objects.all()
    return render(request, 'customer/vidhyas_package/vidhyas_package.html',
                  {'form': form, 'diet_Plan_Package': diet_Plan_Package})


def delete_vidhyas_package(request):
    diet_Plan_Package = get_object_or_404(Diet_Plan_Package, pk=request.POST.get('trash_id'))
    diet_Plan_Package.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
