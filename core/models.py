from django.db import models

# Create your models here.
class Transaction(models.Model):
    class Meta:
        db_table = "transaction"

    status_choices = [ 
        ("new", "new"), 
        ("closed", "closed"),
        ("assigned", "assigned")        
        ]

    country_code_choices = [
        ("54", "54"),
        ("55", "55"),
        ("56", "56")
        ]

    riskscore = models.FloatField(default="0.0")
    transaction_date = models.DateTimeField(auto_now=False)
    transaction_id = models.CharField(max_length=255, null=True)
    transaction_type = models.CharField(max_length=255, null=True)
    remarks = models.CharField(max_length=255, null=True, default="")
    status = models.CharField(max_length=255, default='new', choices=status_choices)
    country_code = models.CharField(max_length=255, null=True, choices=country_code_choices, default=True)
    # Source Details
    customer_id = models.CharField(max_length=255, null=True)
    dr_channel = models.CharField(max_length=255, null=True)
    dr_currency = models.CharField(max_length=255, null=True)    
    customer_name = models.CharField(max_length=255, null=True)
    dr_amount = models.DecimalField(max_digits=15, decimal_places=2)
    dr_account = models.CharField(max_length=255, null=True, default="")
    # Destionation
    customerId = models.CharField(max_length=255, null=True)
    cr_channel = models.CharField(max_length=255, null=True)
    cr_currency = models.CharField(max_length=255, null=True)
    customer_name = models.CharField(max_length=255, null=True)
    cr_amount = models.DecimalField(max_digits=15, decimal_places=2)
    cr_account = models.CharField(max_length=255, null=True, default="")
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)