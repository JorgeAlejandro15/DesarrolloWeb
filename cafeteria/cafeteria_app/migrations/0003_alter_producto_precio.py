# Generated by Django 4.1.7 on 2023-05-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria_app', '0002_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]
