# Generated by Django 3.1.3 on 2021-09-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210926_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='order_date',
            field=models.DateField(),
        ),
    ]