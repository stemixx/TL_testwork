from django.urls import path
from employee.views import DepartmentListView


urlpatterns = [
    path('', DepartmentListView.as_view(), name='department-list'),
]