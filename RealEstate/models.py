from django.db import models
from uuid import uuid4

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=100, blank= False, default="Enter Property Name")
    property_type = models.CharField(max_length=100, choices= [("Residential","Residential"),("Commercial","Commercial")],blank = False,  default= "Residential")
    property_area = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Area in sqft")
    property_address = models.TextField(max_length=300, blank = False, null=False, default= "Enter Address")
    property_state = models.CharField(max_length=100, blank = False, null=False, default= "Enter State")
    property_owner = models.CharField(max_length=100)
    property_owner_contact = models.IntegerField(blank= False, null = False, default=0)
    property_owner_email = models.EmailField(max_length=100)
    property_image = models.ImageField(upload_to='static/images/')
    property_units = models.IntegerField(blank= False, null = False, default=1)
    property_description = models.TextField(max_length=300, blank = False, null=False, default= "Enter Description")

    def __str__(self):
        return f"Property: " + self.property_name



class Property_Unit(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_id = models.AutoField(primary_key = True)
    unit_name = models.CharField(null = False, blank = False, max_length = 100, default= "Enter the Unit Name")
    number_of_rooms = models.IntegerField(null = False, blank = False, default= 1)
    number_of_bathrooms = models.IntegerField(null = False, blank = False, default= 1)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Price in INR")
    unit_furnished = models.BooleanField(default=False)
    unit_description = models.TextField(max_length=300, blank = False, null=False, default= "Enter Description")
    unit_availablity = models.CharField(max_length=100, choices= [("Available","Available"),("Leased","Leased")], default="Available")
    
    def __str__(self):
        return f"Unit: " + self.unit_name



class Lease_Agreement(models.Model):
    unit_id = models.OneToOneField(Property_Unit, on_delete=models.CASCADE)
    agreement_id = models.AutoField(primary_key = True)
    agreement_start_date = models.DateField()
    agreement_end_date = models.DateField()
    agreement_duration = models.IntegerField(default=1, verbose_name="Duration in months")
    agreement_rent = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Rent in INR")
    agreement_security_deposit = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Security Deposit in INR")
    late_payment_penalty = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Penalty in INR")
    payment_date = models.DateField(verbose_name="Payment Date every month")
    payment_grace_period = models.IntegerField(default=0, verbose_name="Grace Period in days")
    agreement_termination = models.BooleanField(default=False)
    agreement_termination_date = models.DateField(null=True, blank=True)
    owner = models.CharField(max_length=100)
    tenant = models.CharField(max_length=100)
    owner_contact = models.IntegerField(blank= False, null = False, default=0)  
    tenant_contact = models.IntegerField(blank= False, null = False, default=0)
    owner_email = models.EmailField(max_length=100)
    tenant_email = models.EmailField(max_length=100)
    agreement_description = models.TextField(max_length=300, blank = False, null=False, default= "Enter Description")

    def __str__(self):
        return f"Lease Agreement between " + self.owner + " and " + self.tenant + " for " + self.unit_id.unit_name + " from" + self.agreement_start_date + " to " + self.agreement_end_date