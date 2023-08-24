from django.urls import path, include

from django.contrib import admin
# from vidhyas_api.views import ObtainAuthTokenView

urlpatterns = [
    path('admin/', admin.site.urls),            # default admin
    path('api/', include("vidhyas_api.urls")),  # include api
    path('', include("authentication.urls")),   # include auth
    path('', include('index.urls')),             # include index
    path('', include('humanresource.urls')),  # Use 'department/' as the path
    ]