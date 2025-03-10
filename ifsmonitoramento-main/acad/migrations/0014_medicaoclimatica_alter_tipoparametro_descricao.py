# Generated by Django 5.0.8 on 2025-02-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0013_tiposala'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicaoClimatica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('temperatura', models.FloatField()),
                ('umidade', models.FloatField()),
                ('sensacao_termica', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='tipoparametro',
            name='descricao',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Temperatura'),
        ),
    ]
