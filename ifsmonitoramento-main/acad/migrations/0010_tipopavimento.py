# Generated by Django 5.0.8 on 2025-01-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0009_tipoparametro'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPavimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Sensor Lógico')),
                ('sigla', models.CharField(max_length=10, unique=True, verbose_name='Sigla')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Pavimento',
                'verbose_name_plural': 'Tipos de Pavimentos',
                'db_table': 'tb_tipo_pavimento',
            },
        ),
    ]
