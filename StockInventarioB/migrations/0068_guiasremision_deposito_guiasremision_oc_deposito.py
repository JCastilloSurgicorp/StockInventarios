# Generated by Django 4.2.16 on 2024-12-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0067_stocksinventario_descr_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='guiasremision',
            name='deposito',
            field=models.CharField(blank=True, db_column='DEPOSITO', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='guiasremision_oc',
            name='deposito',
            field=models.CharField(blank=True, db_column='DEPOSITO', max_length=15, null=True),
        ),
    ]
