# Generated by Django 3.1.3 on 2021-09-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210926_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='customer_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sale',
            name='order_date',
            field=models.IntegerField(),
        ),
    ]
