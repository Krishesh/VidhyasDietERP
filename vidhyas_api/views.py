from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView


class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}
        print(request.data)
        username = request.data['username']
        password = request.data['password']
        print(username)
        print(password)
        account = authenticate(username=username, password=password)
        if account:
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['username'] = username
            context['password'] = password
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'
        print(context)
        return Response(context)