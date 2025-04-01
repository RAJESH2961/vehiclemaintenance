from djongo import models
from datetime import date
import uuid

# Customer Model
class Customer(models.Model):
    customer_number = models.CharField(max_length=20, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    registration_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.customer_number})"

    class Meta:
        db_table = "customers"

# Vehicle Model (Updated to Link with Customer)
class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Truck', 'Truck'),
        ('Bike', 'Bike'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Sold', 'Sold'),
        ('Scrapped', 'Scrapped'),
    ]
    
    license_plate = models.CharField(max_length=15, unique=True)
    owner = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='vehicles'
    )  # Link Vehicle to Customer
    
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES, default='Car')
    registration_date = models.DateField(default=date.today)
    last_serviced_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f"{self.license_plate} - {self.owner.first_name} {self.owner.last_name}"

    class Meta:
        db_table = "vehicles"

# MaintenanceLog Model
class MaintenanceLog(models.Model):
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    mechanic_name = models.CharField(max_length=100, blank=True, null=True)
    warranty_applied = models.BooleanField(default=False)
    next_service_due_date = models.DateField(null=True, blank=True)
    
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="maintenance_logs"
    )

    def __str__(self):
        return f"Log for {self.vehicle.license_plate} on {self.service_date}"

    class Meta:
        db_table = "maintenance_logs"
