from django.urls import path
from .views import (EmployeeListView,EmployeeDetailView,EmployeeCreateView,EmployeeUpdateView,EmployeeDeleteView)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/new/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
]