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
    remarks = models.CharField(max_length=255, default="")
    transaction_date = models.DateTimeField(auto_now=False)    
    transaction_type = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, default='new', choices=status_choices)
    country_code = models.CharField(max_length=255, choices=country_code_choices, default=True)
    # Source Details
    source_channel = models.CharField(max_length=255)
    source_currency = models.CharField(max_length=255)
    source_account = models.CharField(max_length=255, default="")
    source_amount = models.DecimalField(max_digits=15, decimal_places=2)
    # Destionation
    destination_channel = models.CharField(max_length=255)
    destination_currency = models.CharField(max_length=255)
    destination_account = models.CharField(max_length=255, default="")
    destination_amount = models.DecimalField(max_digits=15, decimal_places=2)
    

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)