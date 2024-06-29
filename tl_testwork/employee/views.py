from django.views.generic import ListView
from .models import Department, Employee


class DepartmentListView(ListView):
    model = Department

    template_name = 'employee/employee_list.html'
    context_object_name = 'departments'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        self.department = Department.objects.get(slug=self.kwargs['slug'])
        queryset = Employee.objects.filter(department=self.department)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.department
        return context
