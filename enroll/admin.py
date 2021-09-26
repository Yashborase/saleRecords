from .models import Sale
from django.contrib import admin
from .models import Sale
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Sale)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('order_ID','order_date','order_quantity','sales_p','ship_mode','profit_p',
                'unit_price','customer_name','customer_segment','product_category')

