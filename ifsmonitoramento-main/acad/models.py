from django.db import models
from datetime import datetime


# Create your models here.

class TipoSensor(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Sensor")
    limite_inferior_permitido = models.FloatField(null=True, blank=True, verbose_name="Limite Inferior Permitido")
    limite_superior_permitido = models.FloatField(null=True, blank=True, verbose_name="Limite Superior Permitido")
    unidade = models.CharField(max_length=45, null=True, blank=True, verbose_name="Unidade")

    class Meta:
        db_table = 'tb_tipo_sensor'
        verbose_name = "Tipo de Sensor"
        verbose_name_plural = "Tipos de Sensores"

    def __str__(self):
        return self.descricao

class TipoSensorFisico(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Sensor Físico")
    sigla = models.CharField(max_length=10, unique=True, verbose_name="Sigla")
    descricao = models.CharField(max_length=150, null=True, blank=True, verbose_name="Descrição")
    tensao_min = models.FloatField(null=True, blank=True, verbose_name="Tensão Mínima")
    tensao_max = models.FloatField(null=True, blank=True, verbose_name="Tensão Máxima")
  
    class Meta:
        db_table = 'tb_sensor_fisico'
        verbose_name = "Tipo de Sensor Físico"
        verbose_name_plural = "Tipos de Sensores Físicos"
  
    def __str__(self):
        return self.nome

class TipoSensorLogico(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Sensor Lógico")
    id_sensor_fisico = models.ForeignKey(
        'TipoSensorFisico',
        on_delete=models.PROTECT,
        db_column="id_sensor_fisico",
        verbose_name="Sensor Físico",
        null=True,
        blank=True
    )
    id_tipo_sensor = models.ForeignKey(
        'TipoSensor',
        on_delete=models.PROTECT,
        db_column="id_tipo",  # Alterado para 'id_tipo' conforme o SQL
        verbose_name="Tipo de Sensor",
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'tb_sensor_logico'
        verbose_name = "Tipo de Sensor Lógico"
        verbose_name_plural = "Tipos de Sensores Lógicos"

    def __str__(self):
        return self.descricao


class TipoParametro(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Parâmetro")
    valor = models.FloatField(null=True, blank=True, verbose_name="Valor")
    id_sensor_logico = models.ForeignKey(
        'TipoSensorLogico',
        on_delete=models.PROTECT,
        db_column="id_sensor_logico",
        verbose_name="Sensor Lógico",
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'tb_parametro'
        verbose_name = "Tipo de Parâmetro"
        verbose_name_plural = "Tipos de Parâmetros"

    def __str__(self):
        return self.nome



class TipoPavimento(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Pavimento")
  
    class Meta:
        db_table = 'tb_pavimento'
        verbose_name = "Tipo de Pavimento"
        verbose_name_plural = "Tipos de Pavimentos"
  
    def __str__(self):
        return self.nome


class TipoOrientacao(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Orientação")
  
    class Meta:
        db_table = 'tb_orientacao'
        verbose_name = "Tipo de Orientação"
        verbose_name_plural = "Tipos de Orientações"
  
    def __str__(self):
        return self.nome


class TipoSala(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Sala")
    sigla = models.CharField(max_length=10, verbose_name="Sigla")
    pavimento = models.ForeignKey(
        TipoPavimento,
        on_delete=models.PROTECT,
        db_column="id_pavimento"  # Corrigido (antes estava "id_pavimnto")
    )
    orientacao = models.ForeignKey(
        TipoOrientacao,
        on_delete=models.PROTECT,
        db_column="id_orientacao"
    )
  
    class Meta:
        db_table = 'tb_sala'
        managed = False 
        verbose_name = "Tipo de Sala"
        verbose_name_plural = "Tipos de Salas"
  
    def __str__(self):
        return self.nome

from django.db import models

class MedicaoClimatica(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)  # modelo para adicionar do código principal
    temperatura = models.FloatField() 
    umidade = models.FloatField()  
    sensacao_termica = models.FloatField()  

    def __str__(self):
        return f"{self.data_hora} - Temp: {self.temperatura}°C, Umidade: {self.umidade}%"


class Leitura(models.Model):  # modelo para adicionar do código principal
    id_sala = models.ForeignKey(
        'TipoSala',  # Referencia a tabela TipoSala
        on_delete=models.PROTECT,
        db_column="id_sala",
        verbose_name="Sala"
    )
    data_hora = models.DateTimeField(verbose_name="Data e Hora")

    class Meta:
        db_table = 'tb_leitura'
        verbose_name = "Leitura"
        verbose_name_plural = "Leituras"

    def __str__(self):
        return f"Leitura em {self.data_hora} - Sala {self.id_sala}"

class LeituraSensor(models.Model):  # modelo para adicionar do código principal
    id_sensor_logico = models.ForeignKey(
        'TipoSensorLogico',  # Referência à tabela TipoSensorLogico
        on_delete=models.PROTECT,
        db_column="id_sensor_logico",
        verbose_name="Sensor Lógico"
    )
    id_leitura = models.ForeignKey(
        'Leitura',  # Referência à tabela Leitura
        on_delete=models.PROTECT,
        db_column="id_leitura",
        verbose_name="Leitura"
    )
    valor = models.FloatField(verbose_name="Valor")

    class Meta:
        db_table = 'tb_leitura_sensor'
        verbose_name = "Leitura de Sensor"
        verbose_name_plural = "Leituras de Sensores"

    def __str__(self):
        return f"Leitura {self.id_leitura} - Sensor {self.id_sensor_logico}: {self.valor}"


# Models para Views de Agrupamento

# View de 5 Minutos
class VWAgrupamento5Minutos(models.Model):
    data_hora = models.DateTimeField(verbose_name="Data", primary_key=True)
    nome_sensor_fisico = models.CharField(max_length=100, verbose_name="Sensor Físico")
    tipo_sensor = models.CharField(max_length=100, verbose_name="Tipo de Sensor")
    unidade_sensor = models.CharField(max_length=20, verbose_name="Unidade")
    nome_sala = models.CharField(max_length=100, verbose_name="Sala")
    sigla_sala = models.CharField(max_length=10, verbose_name="Sigla Sala")
    valor_medio = models.FloatField(verbose_name="Valor Médio")

    class Meta:
        managed = False  # Não criar tabela no banco
        db_table = 'vw_agrupamento_5_minutos'

    def __str__(self):
        return f"{self.data_hora} - {self.nome_sensor_fisico} - {self.valor_medio}"

# View de 15 Minutos
class VWAgrupamento15Minutos(models.Model):
    data_hora = models.DateTimeField(verbose_name="Data", primary_key=True)
    nome_sensor_fisico = models.CharField(max_length=100, verbose_name="Sensor Físico")
    tipo_sensor = models.CharField(max_length=100, verbose_name="Tipo de Sensor")
    unidade_sensor = models.CharField(max_length=20, verbose_name="Unidade")
    nome_sala = models.CharField(max_length=100, verbose_name="Sala")
    sigla_sala = models.CharField(max_length=10, verbose_name="Sigla Sala")
    valor_medio = models.FloatField(verbose_name="Valor Médio")

    class Meta:
        managed = False
        db_table = 'vw_agrupamento_15_minutos'

    def __str__(self):
        return f"{self.data_hora} - {self.nome_sensor_fisico} - {self.valor_medio}"

# View de 30 Minutos
class VWAgrupamento30Minutos(models.Model):
    data_hora = models.DateTimeField(verbose_name="Data", primary_key=True)
    nome_sensor_fisico = models.CharField(max_length=100, verbose_name="Sensor Físico")
    tipo_sensor = models.CharField(max_length=100, verbose_name="Tipo de Sensor")
    unidade_sensor = models.CharField(max_length=20, verbose_name="Unidade")
    nome_sala = models.CharField(max_length=100, verbose_name="Sala")
    sigla_sala = models.CharField(max_length=10, verbose_name="Sigla Sala")
    valor_medio = models.FloatField(verbose_name="Valor Médio")

    class Meta:
        managed = False
        db_table = 'vw_agrupamento_30_minutos'

    def __str__(self):
        return f"{self.data_hora} - {self.nome_sensor_fisico} - {self.valor_medio}"

# View de 60 Minutos
class VWAgrupamento60Minutos(models.Model):
    data_hora = models.DateTimeField(verbose_name="Data", primary_key=True)
    nome_sensor_fisico = models.CharField(max_length=100, verbose_name="Sensor Físico")
    tipo_sensor = models.CharField(max_length=100, verbose_name="Tipo de Sensor")
    unidade_sensor = models.CharField(max_length=20, verbose_name="Unidade")
    nome_sala = models.CharField(max_length=100, verbose_name="Sala")
    sigla_sala = models.CharField(max_length=10, verbose_name="Sigla Sala")
    valor_medio = models.FloatField(verbose_name="Valor Médio")

    class Meta:
        managed = False
        db_table = 'vw_agrupamento_60_minutos'

    def __str__(self):
        return f"{self.data_hora} - {self.nome_sensor_fisico} - {self.valor_medio}"

# View de 120 Minutos
class VWAgrupamento120Minutos(models.Model):
    data_hora = models.DateTimeField(verbose_name="Data", primary_key=True)
    nome_sensor_fisico = models.CharField(max_length=100, verbose_name="Sensor Físico")
    tipo_sensor = models.CharField(max_length=100, verbose_name="Tipo de Sensor")
    unidade_sensor = models.CharField(max_length=20, verbose_name="Unidade")
    nome_sala = models.CharField(max_length=100, verbose_name="Sala")
    sigla_sala = models.CharField(max_length=10, verbose_name="Sigla Sala")
    valor_medio = models.FloatField(verbose_name="Valor Médio")

    class Meta:
        managed = False
        db_table = 'vw_agrupamento_120_minutos'

    def __str__(self):
        return f"{self.data_hora} - {self.nome_sensor_fisico} - {self.valor_medio}"

# View de 240 Minutos
class VWAgrupamento240Minutos(models.Model):
    data_hora = models.DateTimeField(verbose_name="Data", primary_key=True)
    nome_sensor_fisico = models.CharField(max_length=100, verbose_name="Sensor Físico")
    tipo_sensor = models.CharField(max_length=100, verbose_name="Tipo de Sensor")
    unidade_sensor = models.CharField(max_length=20, verbose_name="Unidade")
    nome_sala = models.CharField(max_length=100, verbose_name="Sala")
    sigla_sala = models.CharField(max_length=10, verbose_name="Sigla Sala")
    valor_medio = models.FloatField(verbose_name="Valor Médio")

    class Meta:
        managed = False
        db_table = 'vw_agrupamento_240_minutos'

    def __str__(self):
        return f"{self.data_hora} - {self.nome_sensor_fisico} - {self.valor_medio}"
