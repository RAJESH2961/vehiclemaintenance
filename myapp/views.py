from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Customer, Vehicle, MaintenanceLog

def home(request):
    today = timezone.now().date()
    two_days_ago = today - timedelta(days=2)
    three_days_later = today + timedelta(days=3)

    # Maintenance logs two days ago
    vehicles_serviced_two_days_ago = MaintenanceLog.objects.filter(
        service_date=two_days_ago,
        vehicle__owner__isnull=False
    )

    customer_remind_info = []
    for log in vehicles_serviced_two_days_ago:
        vehicle = log.vehicle
        customer = vehicle.owner
        if customer:  # Safeguard against missing customers
            customer_remind_info.append({
                'customer_name': f"{customer.first_name} {customer.last_name}",
                'mobile_number': customer.phone_number,
                'license_plate': vehicle.license_plate,
                'vehicle_type': vehicle.vehicle_type,
                'mechanic_name': log.mechanic_name,
                'service_date': log.service_date,
                'description': log.description,
            })

    # Maintenance logs with upcoming service
    vehicles_to_notify = MaintenanceLog.objects.filter(
        next_service_due_date__gt=three_days_later,
        vehicle__owner__isnull=False
    )

    # Sort the logs by next_service_due_date
    vehicles_to_notify_sorted = sorted(vehicles_to_notify, key=lambda log: log.next_service_due_date)

    customers_to_notify = []
    for log in vehicles_to_notify_sorted:
        vehicle = log.vehicle
        customer = vehicle.owner
        if customer:  # Safeguard against missing customers
            customers_to_notify.append({
                'customer_name': f"{customer.first_name} {customer.last_name}",
                'mobile_number': customer.phone_number,
                'email': customer.email,
                'last_service_date': vehicle.last_serviced_date,
                'next_service_due_date': log.next_service_due_date,
                'vehicle_type': vehicle.vehicle_type,
                'license_plate': vehicle.license_plate,
            })

    return render(request, 'index.html', {
        'customers': customers_to_notify,
        'customer_remind_info': customer_remind_info,
    })
