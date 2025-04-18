# Generated by Django 4.2.16 on 2024-11-12 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockInventarioB', '0058_gr_descripcion_descr_prod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojapicking',
            name='gr_id',
            field=models.ForeignKey(db_column='GR_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='StockInventarioB.guiasremision'),
        ),
        migrations.AddField(
            model_name='hojapicking',
            name='gr_oc_id',
            field=models.ForeignKey(db_column='GR_OC_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='StockInventarioB.guiasremision_oc'),
        ),
    ]
