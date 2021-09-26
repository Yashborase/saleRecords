# from django.db import models
from django.db.models.fields import CharField, EmailField,IntegerField,DateTimeField
from django.db import models

import datetime
from django.conf import settings
from django.utils.timezone import make_aware


# Create your models here.
class Sale(models.Model):

    order_ID = models.IntegerField()    
    order_date = models.DateTimeField()
    order_quantity = models.IntegerField()
    sales_p = models.IntegerField()
    ship_mode = models.CharField(max_length=200) 
    profit_p = models.IntegerField()
    unit_price = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    customer_segment =  models.CharField(max_length=200) 
    product_category =  models.CharField(max_length=200) 