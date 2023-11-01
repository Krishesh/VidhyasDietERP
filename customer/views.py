from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import Diet_Plan_Package, Customer
from customer.serializers import Diet_Plan_Package_Serializer, Customer_Serializer


# Create your views here.


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

    '''def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Diet_Plan_Package_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
