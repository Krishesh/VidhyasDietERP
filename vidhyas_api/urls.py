from django.urls import path
from .views import ObtainAuthTokenView
from .views import DepartmentListView, DepartmentDetailView
from .views import EmployeeListView, EmployeeDetailView
from .views import SalaryListView, SalaryDetailView
from .views import PayslipListView, PayslipDetailView
from .views import PlaySlip_CodeListView, PlaySlip_CodeDetailView

app_name = 'vidhyas_api'

urlpatterns = [
    path('test_login', ObtainAuthTokenView.as_view(), name="api_login"),
    path('departments', DepartmentListView.as_view(), name='department-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-create'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('salary/', SalaryListView.as_view(), name='salary-list'),
    path('salary/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
    path('payslip/', PayslipListView.as_view(), name='payslip-list'),
    path('payslip/<int:pk>/', PayslipDetailView.as_view(), name='payslip-detail'),
    path('playSlip_Code/', PlaySlip_CodeListView.as_view(), name='playSlip_Code-list'),
    path('playSlip_Code/<int:pk>/', PlaySlip_CodeDetailView.as_view(), name='playSlip_Code-detail'),
]
