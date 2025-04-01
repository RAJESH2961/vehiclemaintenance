from django.contrib import admin
from .models import Customer, Vehicle, MaintenanceLog

# Customize Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'registration_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('registration_date',)
    ordering = ('-registration_date',)

# Customize Vehicle Admin
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate',  'model', 'year', 'vehicle_type', 'status', 'registration_date', 'last_serviced_date')
    search_fields = ('license_plate', 'owner__first_name', 'owner__last_name', 'model')
    list_filter = ('vehicle_type', 'status', 'registration_date', 'last_serviced_date')
    ordering = ('-registration_date',)
    autocomplete_fields = ('owner',)

# Customize MaintenanceLog Admin
@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service_date', 'description', 'cost', 'mechanic_name', 'warranty_applied', 'next_service_due_date')
    search_fields = ('vehicle__license_plate', 'mechanic_name', 'description')
    list_filter = ('service_date', 'warranty_applied', 'next_service_due_date')
    ordering = ('-service_date',)
    autocomplete_fields = ('vehicle',)
