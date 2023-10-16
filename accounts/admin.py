from django.contrib import admin

from .models import CustomUser, Employee, Customer


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'address', 'contact')
    search_fields = ('email', 'address', 'contact')
    # Add any other customization you want

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_employee')
    search_fields = ('user__email',)
    list_filter = ('is_employee',)
    # Add any other customization you want

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_customer')
    search_fields = ('user__email',)
    list_filter = ('is_customer',)
    # Add any other customization you want

