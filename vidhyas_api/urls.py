from django.urls import path
from .views import ObtainAuthTokenView
from .views import DepartmentListView, DepartmentDetailView
from .views import EmployeeListView, EmployeeDetailView
from .views import SalaryListView, SalaryDetailView
from .views import PayslipListView, PayslipDetailView
from .views import PlaySlip_CodeListView, PlaySlip_CodeDetailView

app_name = 'vidhyas_api'

urlpatterns = [
    path('api/test_login', ObtainAuthTokenView.as_view(), name="api_login"),
    path('api/departments/', DepartmentListView.as_view(), name='departments'),
    path('api/departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-create'),
  
    path('api/employees/', EmployeeListView.as_view(), name='employee-list'),
    path('api/employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
  
    path('api/salary/', SalaryListView.as_view(), name='salary-list'),
    path('api/salary/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
    path('api/payslip/', PayslipListView.as_view(), name='payslip-list'),
    path('api/payslip/<int:pk>/', PayslipDetailView.as_view(), name='payslip-detail'),
    path('api/playSlip_Code/', PlaySlip_CodeListView.as_view(), name='playSlip_Code-list'),
    path('api/playSlip_Code/<int:pk>/', PlaySlip_CodeDetailView.as_view(), name='playSlip_Code-detail'),
]
