# Generated by Django 4.2.16 on 2024-11-05 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0052_alter_hojapicking_empr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hojapicking',
            name='empr_id',
            field=models.ForeignKey(blank=True, db_column='EMPRESA_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='StockInventarioB.si_empresa'),
        ),
    ]