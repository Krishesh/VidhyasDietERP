from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class department_api(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serialized_departments = [{'name': department.name} for department in departments]
        return Response(serialized_departments)
