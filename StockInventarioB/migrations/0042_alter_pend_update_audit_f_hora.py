# Generated by Django 4.2.16 on 2024-10-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0041_pend_update_audit_remove_pend_items_cant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pend_update_audit',
            name='f_hora',
            field=models.DateTimeField(blank=True, db_column='FECHA_HORA', null=True),
        ),
    ]
