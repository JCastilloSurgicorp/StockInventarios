# Generated by Django 5.0.6 on 2024-09-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0018_fact_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojapicking',
            name='ubicacion_sector',
            field=models.CharField(blank=True, db_column='UBICACION_SECTOR', max_length=120, null=True),
        ),
    ]
