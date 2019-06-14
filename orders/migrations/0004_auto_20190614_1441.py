# Generated by Django 2.2.1 on 2019-06-14 14:41

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190613_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(orders.models.StatusChoice('CREATED'), 'CREATED'), (orders.models.StatusChoice('PAYED'), 'PAYED'), (orders.models.StatusChoice('COMPLETED'), 'COMPLETED')], default=orders.models.StatusChoice('CREATED'), max_length=50),
        ),
    ]
