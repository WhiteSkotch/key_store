# Generated by Django 4.2.1 on 2023-06-19 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_money_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='is_payed',
        ),
    ]
