# Generated by Django 5.0.6 on 2024-08-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0010_gr_busqueda'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr_busqueda',
            name='fecha_guia',
            field=models.DateField(blank=True, db_column='FECHA_GUIA', null=True),
        ),
    ]
