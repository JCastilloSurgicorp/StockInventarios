# Generated by Django 5.0.6 on 2024-10-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0025_si_productos_proveedor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksinventario',
            name='descr_deposito',
            field=models.CharField(blank=True, db_column='DESCRIPCION_DEPOSITO', max_length=60, null=True),
        ),
    ]