# Generated by Django 4.0 on 2023-06-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_game_image_alter_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
