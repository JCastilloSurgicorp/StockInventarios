# Generated by Django 4.2.16 on 2024-11-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0057_gr_busqueda_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr_descripcion',
            name='descr_prod',
            field=models.CharField(blank=True, db_column='DESCRIPCION_PRODUCTO', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='gr_descripcion_oc',
            name='descr_prod',
            field=models.CharField(blank=True, db_column='DESCRIPCION_PRODUCTO', max_length=120, null=True),
        ),
    ]
