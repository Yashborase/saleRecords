from django.http import response
from django.shortcuts import render, HttpResponseRedirect
from .forms import lead_register
from .models import Sale
import xlwt
import datetime

from xlutils.copy import copy 
from xlrd import open_workbook
import xlwt
from django.http import HttpResponse
import os
from django.conf import settings


from .resources import SaleResource
from tablib import Dataset
from .models import Sale
from django.contrib import messages

# To Add Lead
def add_show(request):
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        fm = lead_register(request.POST)
        if fm.is_valid():
            oi = fm.cleaned_data['order_ID']
            od = fm.cleaned_data['order_date']
            oq = fm.cleaned_data['order_quantity']
            sp = fm.cleaned_data['sales_p']
            sm = fm.cleaned_data['ship_mode']
            pp = fm.cleaned_data['profit_p']
            up = fm.cleaned_data['unit_price']
            cn = fm.cleaned_data['customer_name']
            cs = fm.cleaned_data['customer_segment']
            pc = fm.cleaned_data['product_category']
            reg = Sale(order_ID=oi, order_date=od, order_quantity=oq,sales_p=sp, ship_mode=sm, profit_p=pp,
            unit_price=up, customer_name=cn, customer_segment=cs,product_category=pc)
            reg.save()
            fm = lead_register()
    else:
        fm = lead_register()
    leads = Sale.objects.all()
    return render(request,'enroll/AddShow.html',{ 'form':fm, 'lead_obj': leads})


#To Update Lead
def update_lead(request,id):
    
    if request.method=='POST':
        lead_data=Sale.objects.get(pk=id)
        fm = lead_register(request.POST, instance=lead_data)
        if fm.is_valid():
            fm.save()
    else:
        lead_data = Sale.objects.get(pk=id)
        fm = lead_register(instance=lead_data)
    return render(request, 'enroll/update.html',{'form':fm})
    


#To Delete lead
def delete_lead(request, id):
    
    if request.method=='POST':
        trash_lead = Sale.objects.get(pk=id)
        trash_lead.delete()
        return HttpResponseRedirect('/')
    
def import_leads(request):
    
    #import pdb;pdb.set_trace()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

   
    columns = ['order Date','Sale Price']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  

    font_style = xlwt.XFStyle()

    rows = Sale.objects.all().values_list('order_date',
                'sales_p')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
    
        
    
def export_leads(request):

    import datetime
    from django.conf import settings
    from django.utils.timezone import make_aware

    naive_datetime = datetime.datetime.now()
    naive_datetime.tzinfo

    settings.TIME_ZONE  
    aware_datetime = make_aware(naive_datetime)
    aware_datetime.tzinfo  
   
    request.method = "POST"
    #import pdb;pdb.set_trace()
    if request.method == 'POST':
        sale_resource = SaleResource()
        dataset = Dataset()
        new_sale = request.FILES["excel_file"]
        
        if not new_sale.name.endswith('.xlsx'):
            messages.info(request,'Wrong Format')
            return HttpResponseRedirect('/') 

        imported_data = dataset.load(new_sale.read(),format='xlsx')
        # import pdb;pdb.set_trace()
        # print([str(x) for x in imported_data])
        for data in imported_data:
            
            data_str=str(data[1])
        
            value = Sale(data[0],data_str,data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
            value.save()  
    return HttpResponseRedirect('/') 
    
