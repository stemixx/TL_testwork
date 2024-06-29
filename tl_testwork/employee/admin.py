from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name', 'parent__name')
    list_filter = ('name', 'parent')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'hire_date', 'salary', 'department')
    search_fields = ('full_name', 'position', 'salary', 'department__name')
    list_filter = ('hire_date', 'department', 'position')
    prepopulated_fields = {"slug": ("full_name",)}
