# Generated by Django 5.0.6 on 2024-10-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0032_si_updateaudit_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='si_updateaudit',
            name='tipo_producto',
            field=models.CharField(blank=True, db_column='TIPO_PRODUCTO', max_length=6),
        ),
    ]
