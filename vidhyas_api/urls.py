from django.urls import path
from .views import ObtainAuthTokenView
from .views import DepartmentListView, DepartmentDetailView
from .views import EmployeeListView, EmployeeDetailView

app_name = 'vidhyas_api'

urlpatterns = [
    path('test_login', ObtainAuthTokenView.as_view(), name="api_login"),
    path('departments', DepartmentListView.as_view(), name='department-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-create'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
