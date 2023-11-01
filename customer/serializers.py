from rest_framework import serializers
import sys
import os
from django.conf import settings

from django.contrib.auth.models import User

from customer.models import Diet_Plan_Package, Customer, Customer_Stats


class Diet_Plan_Package_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Diet_Plan_Package
        fields = '__all__'


class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class Customer_Stats_Serializer(serializers.ModelSerializer):
    # customer_details = serializers.DictField(source='customer', read_only=True,child=serializers.CharField())

    class Meta:
        model = Customer_Stats
        fields = '__all__'
