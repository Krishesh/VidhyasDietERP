from django.urls import path, include

from django.contrib import admin
# from vidhyas_api.views import ObtainAuthTokenView

urlpatterns = [
    path('admin/', admin.site.urls),            # default admin
    path('api/', include("vidhyas_api.urls")),  # include api
    path('', include("user_authentication.urls")),   # include auth
    path('', include("customer.urls")),   # include auth
    path('', include("humanresource.urls")),   # include auth
    path('', include('index.urls')),             # include index
    path('', include('inquiry.urls')),             # include inquiry
    path('', include('registration.urls')),             # include registration
    path('', include('account.urls')),             # include account_list
    path('', include('diet.urls')),             # include diet
]
