from rest_framework import serializers


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    token = serializers.CharField()

