# Generated by Django 5.0.6 on 2024-08-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0011_gr_busqueda_fecha_guia'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr_busqueda',
            name='oc_cliente',
            field=models.CharField(blank=True, db_column='OC_CLIENTE', max_length=20, null=True),
        ),
    ]
