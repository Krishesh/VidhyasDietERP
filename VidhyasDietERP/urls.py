from django.db import router
from django.urls import include, path
from rest_framework import routers

from authentication import admin

urlpatterns = [

    path("admin/", admin.site.urls),
    path('', include('authentication.urls')),


    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

