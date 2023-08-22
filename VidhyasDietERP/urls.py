from django.urls import path, include

from django.contrib import admin
# from vidhyas_api.views import ObtainAuthTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("vidhyas_api.urls")),
    path('', include("authentication.urls")),
]
