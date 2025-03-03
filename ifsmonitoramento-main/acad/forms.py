from django import forms
from .models import TipoSensor
from .models import TipoSensorFisico
from .models import TipoSensorLogico
from .models import TipoParametro
from .models import TipoPavimento
from .models import TipoOrientacao
from .models import TipoSala


class TipoSensorForm(forms.ModelForm):
    class Meta:
        model = TipoSensor
        fields = [ "descricao","limite_inferior_permitido","limite_superior_permitido","unidade"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 3, "cols": 50}),
        }

    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc

class TipoSensorFisicoForm(forms.ModelForm):
    class Meta:
        model = TipoSensorFisico
        fields = ["nome","sigla", "descricao"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 3, "cols": 50}),
        }

    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc

class TipoSensorLogicoForm(forms.ModelForm):
    class Meta:
        model = TipoSensorLogico
        fields = ["descricao","id_sensor_fisico","id_tipo_sensor"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 3, "cols": 50}),
        }

    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc

class TipoParametroForm(forms.ModelForm):# form atualizado 18/02/25
    class Meta:
        model = TipoParametro
        fields = ["nome","valor","id_sensor_logico"]
        

    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc

class TipoPavimentoForm(forms.ModelForm):# form atualizado 18/02/25
    class Meta:
        model = TipoPavimento
        fields = ["nome"]
       

    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc

class TipoOrientacaoForm(forms.ModelForm):# form atualizado 18/02/25
    class Meta:
        model = TipoOrientacao
        fields = ["nome"]
       

    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc

class TipoSalaForm(forms.ModelForm):
    class Meta:
        model = TipoSala
        fields = ["nome","sigla","pavimento","orientacao"]
        
    def clean_tipo(self):
        tipo = self.cleaned_data.get("nome")
        if "inválido" in tipo.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return tipo

    def clean_descricao(self):
        desc = self.cleaned_data.get("descricao")
        
        return desc
#edição 12/02/24
class RelatorioFiltroForm(forms.Form):
    # Filtro por data
    data_inicio = forms.DateField(
        required=False,
        label="Data Inicial",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    data_fim = forms.DateField(
        required=False,
        label="Data Final",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    # Filtro por sala
    sala = forms.ModelChoiceField(
        queryset=TipoSala.objects.all(),
        required=False,
        label="Sala",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    # Filtro por tipo de sensor
    tipo_sensor = forms.ModelChoiceField(
        queryset=TipoSensor.objects.all(),
        required=False,
        label="Descrição",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    # Filtro por sensor físico
    sensor_fisico = forms.ModelChoiceField(
        queryset=TipoSensorFisico.objects.all(),
        required=False,
        label="Sensor",
        widget=forms.Select(attrs={"class": "form-select"})
    )

class ValoresCriticosFiltroForm(forms.Form):
    # Filtro por data
    data_inicio = forms.DateField(
        required=False,
        label="Data Inicial",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    data_fim = forms.DateField(
        required=False,
        label="Data Final",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    # Filtro por tipo de sensor
    tipo_sensor = forms.ModelChoiceField(
        queryset=TipoSensor.objects.all(),
        required=False,
        label="Tipo de Sensor",
        widget=forms.Select(attrs={"class": "form-select"})
    )

class HistoricoPersonalizadoFiltroForm(forms.Form):
    sala = forms.ModelChoiceField(
        queryset=TipoSala.objects.all(),
        required=False,
        label="Sala",
        widget=forms.Select(attrs={'class': 'form-select rounded-pill'})
    )
    tipo_sensor = forms.ModelChoiceField(
        queryset=TipoSensor.objects.all(),
        required=False,
        label="Tipo de Sensor",
        widget=forms.Select(attrs={'class': 'form-select rounded-pill'})
    )
    data_inicio = forms.DateTimeField(
        required=False,
        label="Data Início",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control rounded-pill'})
    )
    data_fim = forms.DateTimeField(
        required=False,
        label="Data Fim",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control rounded-pill'})
    )
    intervalo = forms.ChoiceField(
        choices=[
            ('5', '5 Minutos'),
            ('15', '15 Minutos'),
            ('30', '30 Minutos'),
            ('60', '60 Minutos'),
            ('120', '120 Minutos'),
            ('240', '240 Minutos'),
        ],
        required=True,
        label="Intervalo de Agrupamento",
        widget=forms.Select(attrs={'class': 'form-select rounded-pill'})
    )

    def get_model(self):
        """
        Retorna o Model correto baseado no intervalo selecionado.
        """
        intervalo = self.cleaned_data.get('intervalo')
        if intervalo == '5':
            from acad.models import VWAgrupamento5Minutos
            return VWAgrupamento5Minutos
        elif intervalo == '15':
            from acad.models import VWAgrupamento15Minutos
            return VWAgrupamento15Minutos
        elif intervalo == '30':
            from acad.models import VWAgrupamento30Minutos
            return VWAgrupamento30Minutos
        elif intervalo == '60':
            from acad.models import VWAgrupamento60Minutos
            return VWAgrupamento60Minutos
        elif intervalo == '120':
            from acad.models import VWAgrupamento120Minutos
            return VWAgrupamento120Minutos
        elif intervalo == '240':
            from acad.models import VWAgrupamento240Minutos
            return VWAgrupamento240Minutos
        else:
            return None

class RelatorioLeiturasFiltroForm(forms.Form):
    # Filtro por sala
    sala = forms.ModelChoiceField(
        queryset=TipoSala.objects.all(),
        required=False,
        label="Sala",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    # Filtro por data de leitura (data_hora)
    data_inicio = forms.DateField(
        required=False,
        label="Data de Leitura (Início)",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    data_fim = forms.DateField(
        required=False,
        label="Data de Leitura (Fim)",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    # Filtro por tipo de sensor lógico
    sensor_logico = forms.ModelChoiceField(
        queryset=TipoSensorLogico.objects.all(),
        required=False,
        label="Tipo de Sensor",
        widget=forms.Select(attrs={"class": "form-select"})
    )


class RelatorioSensoresFiltroForm(forms.Form):
    tipo_sensor = forms.ModelChoiceField(
        queryset=TipoSensor.objects.all(),
        required=False,
        label="Tipo de Sensor",
        empty_label="Todos os Tipos"
    )

    sensor_fisico = forms.ModelChoiceField(
        queryset=TipoSensorFisico.objects.all(),
        required=False,
        label="Sensor Físico",
        empty_label="Todos os Sensores Físicos"
    )

    sensor_logico = forms.ModelChoiceField(
        queryset=TipoSensorLogico.objects.all(),
        required=False,
        label="Sensor Lógico",
        empty_label="Todos os Sensores Lógicos"
    )

    limite_inferior = forms.FloatField(
        required=False,
        label="Limite Inferior Permitido"
    )

    limite_superior = forms.FloatField(
        required=False,
        label="Limite Superior Permitido"
    )
