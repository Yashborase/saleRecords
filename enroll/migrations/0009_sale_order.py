# Generated by Django 3.1.3 on 2021-09-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_auto_20210926_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]