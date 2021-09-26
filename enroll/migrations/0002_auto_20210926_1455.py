# Generated by Django 3.1.3 on 2021-09-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ID', models.DateTimeField()),
                ('order_date', models.DateTimeField()),
                ('order_quantity', models.IntegerField()),
                ('sales_p', models.IntegerField()),
                ('ship_mode', models.CharField(max_length=200)),
                ('profit_p', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('customer_name', models.IntegerField()),
                ('customer_segment', models.CharField(max_length=200)),
                ('product_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
