# Generated by Django 4.0 on 2023-06-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_money_transaction_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
