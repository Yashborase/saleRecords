from django.core import validators
from django import forms
from django.db.models.fields import EmailField
from django.forms import widgets
from .models import Sale 

class lead_register(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['order_ID','order_date','order_quantity','sales_p','ship_mode','profit_p',
                'unit_price','customer_name','customer_segment','product_category']
        # widgets = {
        #     # 'name' : forms.TextInput(attrs={'class':'form-control'}),
        #     # 'email' : forms.EmailInput(attrs={'class':'form-control'}),
        #     # 'assignee' : forms.TextInput(attrs={'class':'form-control'}),
        #     'order_ID' : forms.IntegerField(),
        #     'order_date' : forms.DateField(),
        #     'order_quantity' : forms.IntegerField(),
        #     'sales_p' : forms.IntegerField(),
        #     'ship_mode' : forms.TextInput(),
        #     'profit_p' : forms.IntegerField(),
        #     'unit_price' : forms.IntegerField(),
        #     'customer_name' : forms.TextInput(),
        #     'customer_segment' : forms.TextInput(),
        #     'product_category' : forms.TextInput(),
        # }
        