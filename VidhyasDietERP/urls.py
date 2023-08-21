from django.urls import path

from vidhyas_api.views import CustomObtainAuthToken

urlpatterns = [
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
]
