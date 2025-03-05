from django.db import models
from uuid import uuid4

class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank= False, default="Enter Property Name")
    type = models.CharField(max_length=100, choices= [("Residential","Residential"),("Commercial","Commercial")],blank = False,  default= "Residential")
    area = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Area in sqft")
    address = models.TextField(max_length=300, blank = False, null=False, default= "Enter Address")
    state = models.CharField(max_length=100, blank = False, null=False, default= "Enter State")
    owner = models.CharField(max_length=100)
    owner_contact = models.IntegerField(blank= False, null = False, default=0)
    owner_email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='static/images/', null = True, blank = True)
    units = models.IntegerField(blank= False, null = False, default=1)
    description = models.TextField(max_length=300, blank = False, null=False, default= "Enter Description", editable= True)

    def __str__(self):
        return f"Property: " + self.name



class Property_Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    id = models.AutoField(primary_key = True)
    name = models.CharField(null = False, blank = False, max_length = 100, default= "Enter the Unit Name")
    number_of_rooms = models.IntegerField(null = False, blank = False, default= 1)
    number_of_bathrooms = models.IntegerField(null = False, blank = False, default= 1)
    rent = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Price in INR")
    furnished = models.BooleanField(default=False)
    description = models.TextField(max_length=300, blank = False, null=False, default= "Enter Description")
    availablity = models.CharField(max_length=100, choices= [("Available","Available"),("Leased","Leased")], default="Available")
    
    def __str__(self):
        return f"Unit: " + self.name



class Lease_Agreement(models.Model):
    unit= models.OneToOneField(Property_Unit, on_delete=models.CASCADE)
    id = models.AutoField(primary_key = True)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(default=1, verbose_name="Duration in months")
    rent = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Rent in INR")
    security_deposit = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Security Deposit in INR")
    late_payment_penalty = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name="Penalty in INR")
    payment_date = models.DateField(verbose_name="Payment Date every month")
    payment_grace_period = models.IntegerField(default=0, verbose_name="Grace Period in days")
    owner = models.CharField(max_length=100)
    tenant = models.CharField(max_length=100)
    owner_contact = models.IntegerField(blank= False, null = False, default=0)  
    tenant_contact = models.IntegerField(blank= False, null = False, default=0)
    owner_email = models.EmailField(max_length=100)
    tenant_email = models.EmailField(max_length=100)
    description = models.TextField(max_length=300, blank = False, null=False, default= "Enter Description")

    def __str__(self):
        return f"Lease Agreement between " + self.owner + " and " + self.tenant + " for " + self.unit_id.unit_name + " from" + self.agreement_start_date + " to " + self.agreement_end_date