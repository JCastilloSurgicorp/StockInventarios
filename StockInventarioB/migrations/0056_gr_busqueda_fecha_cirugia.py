# Generated by Django 4.2.16 on 2024-11-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0055_pend_guias'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr_busqueda',
            name='fecha_cirugia',
            field=models.DateField(blank=True, db_column='FECHA_CIRUGIA', null=True),
        ),
    ]
