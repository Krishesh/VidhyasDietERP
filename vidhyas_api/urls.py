from django.urls import path
from .views import ObtainAuthTokenView

app_name = 'vidhyas_api'

urlpatterns = [
    path('test_login', ObtainAuthTokenView.as_view(), name="api_login"),

]
