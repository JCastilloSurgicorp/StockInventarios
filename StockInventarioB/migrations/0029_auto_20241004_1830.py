# Generated by Django 5.0.6 on 2024-10-04 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0028_auto_20241004_1805'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE STOCKS_INVENTARIO ADD RV ROWVERSION'),
    ]
