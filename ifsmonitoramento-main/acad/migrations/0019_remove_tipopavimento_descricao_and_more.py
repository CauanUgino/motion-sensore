# Generated by Django 5.0.8 on 2025-02-09 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0018_tipoparametro_id_sensor_logico_tipoparametro_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipopavimento',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='tipopavimento',
            name='sigla',
        ),
    ]
