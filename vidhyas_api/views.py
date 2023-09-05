from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status  # Import the status module
from django.urls import path

from humanresource.models import Department, Employee, Salary, Payslip, PlaySlip_Code
from vidhyas_api.serializers import DepartmentSerializer, EmployeeSerializer, SalarySerializer, PayslipSerializer, PlaySlip_CodeSerializer

# Auth

class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(password)
        account = authenticate(request, username=username, password=password)
        if account is not None:
            context['response'] = 'success'
            context['pk'] = account.pk
            context['username'] = username
            context['password'] = password
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'
        print(context)
        status_code = status.HTTP_200_OK if account else status.HTTP_401_UNAUTHORIZED
        return Response(context, status=status_code)

#department

class DepartmentListView(APIView):

    def get(self, request, format=None):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetailView(APIView):


    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# for employ

class EmployeeListView(APIView):

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# for Salary

class SalaryListView(APIView):

    def get(self, request, format=None):
        salary = Salary.objects.all()
        serializer = SalarySerializer(salary, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaryDetailView(APIView):

    def get_object(self, pk):
        try:
            return Salary.objects.get(pk=pk)
        except Salary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        salary = self.get_object(pk)
        serializer = SalarySerializer(salary)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        salary = self.get_object(pk)
        serializer = SalarySerializer(salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        salary = self.get_object(pk)
        salary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# for payslip

class PayslipListView(APIView):

    def get(self, request, format=None):
        payslip = Payslip.objects.all()
        serializer = PayslipSerializer(payslip, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PayslipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PayslipDetailView(APIView):

    def get_object(self, pk):
        try:
            return Payslip.objects.get(pk=pk)
        except Payslip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        payslip = self.get_object(pk)
        serializer = PayslipSerializer(payslip)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payslip = self.get_object(pk)
        serializer = PayslipSerializer(payslip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payslip = self.get_object(pk)
        payslip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# for playSlip_Code

class PlaySlip_CodeListView(APIView):

    def get(self, request, format=None):
        playSlip_Code = Payslip.objects.all()
        serializer = PayslipSerializer(playSlip_Code, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaySlip_CodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaySlip_CodeDetailView(APIView):

    def get_object(self, pk):
        try:
            return PlaySlip_Code.objects.get(pk=pk)
        except PlaySlip_Code.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        playSlip_Code = self.get_object(pk)
        serializer = PlaySlip_CodeSerializer(playSlip_Code)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        playSlip_Code = self.get_object(pk)
        serializer = PlaySlip_CodeSerializer(playSlip_Code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        playSlip_Code = self.get_object(pk)
        playSlip_Code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)