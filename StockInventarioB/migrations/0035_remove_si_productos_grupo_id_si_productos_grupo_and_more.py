# Generated by Django 4.2.16 on 2024-10-09 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0034_alter_fact_updateaudit_estado_new_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='si_productos',
            name='grupo_id',
        ),
        migrations.AddField(
            model_name='si_productos',
            name='grupo',
            field=models.CharField(blank=True, db_column='GRUPO', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='si_productos',
            name='proveedor_id',
            field=models.ForeignKey(blank=True, db_column='PROVEEDOR_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='StockInventarioB.hp_proveedor'),
        ),
    ]