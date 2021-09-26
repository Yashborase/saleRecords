from .models import Sale
from import_export import resources


class SaleResource(resources.ModelResource):
    class Meta:
        model = Sale
        skip_unchanged = True
        report_skipped = True
        # exclude = ('id',)
        import_id_fields = ('order_ID','order_date','order_quantity','sales_p','ship_mode','profit_p',
                'unit_price','customer_name','customer_segment','product_category')

