from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status  # Import the status module


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
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['username'] = username
            context['password'] = password
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'
        print(context)
        status_code = status.HTTP_200_OK if account else status.HTTP_401_UNAUTHORIZED
        return Response(context, status=status_code)