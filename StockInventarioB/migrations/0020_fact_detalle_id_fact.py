# Generated by Django 5.0.6 on 2024-09-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0019_hojapicking_ubicacion_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact_detalle',
            name='id_fact',
            field=models.IntegerField(blank=True, db_column='ID_FACT', null=True),
        ),
    ]
