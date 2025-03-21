# Generated by Django 4.2.16 on 2024-11-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0060_auto_20241113_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojapicking',
            name='cliente',
            field=models.CharField(blank=True, db_column='NOMBRE_CLIENTE', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='hojapicking',
            name='motivo',
            field=models.CharField(blank=True, db_column='MOTIVO_TRASLADO', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hojapicking',
            name='tipo_pedido',
            field=models.CharField(blank=True, db_column='TIPO_PEDIDO', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hojapicking',
            name='ubicacion_sector',
            field=models.CharField(blank=True, db_column='UBICACION_SECTOR', max_length=120, null=True),
        ),
    ]
