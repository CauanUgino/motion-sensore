# Generated by Django 5.0.8 on 2025-02-13 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0020_remove_tipoorientacao_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoparametro',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='tiposensorlogico',
            name='id_tipo',
        ),
        migrations.AddField(
            model_name='tiposensorlogico',
            name='id_tipo_sensor',
            field=models.ForeignKey(blank=True, db_column='id_tipo_sensor', null=True, on_delete=django.db.models.deletion.PROTECT, to='acad.tiposensor', verbose_name='Tipo de Sensor'),
        ),
    ]
