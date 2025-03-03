from django.shortcuts import render #método de redenização
from django import forms
from django.db import connection
from datetime import timedelta
from django.utils import timezone
from datetime import datetime
from django.template.loader import get_template
from xhtml2pdf import pisa  # Para geração de PDFs
from django.http import HttpResponse # método para atender as requisições dos usuários
from django.db.models import F, Count, Q  # Adicione F aqui
from django.core.paginator import Paginator
from django.db.models import Avg, F, Func, Count
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)


from .models import TipoSensor
from .forms import TipoSensorForm
from .forms import TipoSensorFisicoForm
from .models import TipoSensorFisico
from .forms import TipoSensorLogicoForm
from .models import TipoSensorLogico
from .forms import TipoParametroForm
from .models import TipoParametro
from .forms import TipoPavimentoForm
from .models import TipoPavimento
from .forms import TipoOrientacaoForm
from .models import TipoOrientacao
from .forms import TipoSalaForm
from .models import TipoSala
from .models import Leitura, LeituraSensor
from .forms import RelatorioLeiturasFiltroForm
from django.http import JsonResponse
from .models import MedicaoClimatica
from .forms import RelatorioFiltroForm
from .forms import ValoresCriticosFiltroForm
from .forms import HistoricoPersonalizadoFiltroForm
from .forms import RelatorioSensoresFiltroForm
from .models import VWAgrupamento5Minutos
from .models import VWAgrupamento15Minutos
from .models import VWAgrupamento30Minutos 
from .models import VWAgrupamento60Minutos 
from .models import VWAgrupamento120Minutos
from .models import  VWAgrupamento240Minutos

# Create your views here.

def home(request):
    return render(request, "acad/home.html") 

def dados_climaticos(request):
    medicoes = MedicaoClimatica.objects.order_by('data_hora') # Views para adicionar do código principal
    labels = [medicao.data_hora.strftime('%d/%m %H:%M') for medicao in medicoes]  
    temperaturas = [medicao.temperatura for medicao in medicoes]
    umidades = [medicao.umidade for medicao in medicoes]
    sensacoes = [medicao.sensacao_termica for medicao in medicoes]

    return JsonResponse({
        'labels': labels,
        'temperaturas': temperaturas,
        'umidades': umidades,
        'sensacoes': sensacoes
    })

def grafico_view(request):
    return render(request, 'acad/Grafico/grafico.html')  # views para adicionar do código principal

class TipoSensorListView(ListView):
    model = TipoSensor
    fields = ["nome", "descricao"]
    context_object_name = "tipo_sensores" 
    template_name = "acad/TipoSensor/tipo_sensor_list.html"

class TipoSensorCreateView(CreateView):
    model = TipoSensor
    form_class = TipoSensorForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_sensor" 
    template_name = "acad/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorUptadeView(UpdateView):
    model = TipoSensor
    form_class = TipoSensorForm  # Usa o ModelForm criado
    context_object_name = "tipo_sensor"
    template_name = "acad/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorDetailView(DetailView):
    model = TipoSensor
    context_object_name = "tipo_sensor"
    template_name = "acad/TipoSensor/tipo_sensor_detail.html"
    fields = ["tipo", "descricao"]

class TipoSensorDeleteView(DeleteView):
    model = TipoSensor
    context_object_name = "tipo_sensor"
    template_name = "acad/TipoSensor/tipo_sensor_delete.html"
    success_url = reverse_lazy("tipo_sensor_list")


class TipoSensorFisicoListView(ListView):
    model = TipoSensorFisico
    fields = ["nome", "descricao"]
    context_object_name = "tipo_sensores_fisicos" 
    template_name = "acad/TipoSensorFisico/tipo_sensor_fisico_list.html"

class TipoSensorFisicoCreateView(CreateView):
    model = TipoSensorFisico
    form_class = TipoSensorFisicoForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_sensor_fisico" 
    template_name = "acad/TipoSensorFisico/tipo_sensor_fisico_form.html"
    success_url = reverse_lazy("tipo_sensor_fisico_list")

class TipoSensorFisicoUptadeView(UpdateView):
    model = TipoSensorFisico
    form_class = TipoSensorFisicoForm  # Usa o ModelForm criado
    context_object_name = "tipo_sensor_fisico"
    template_name = "acad/TipoSensorFisico/tipo_sensor_fisico_form.html"
    success_url = reverse_lazy("tipo_sensor_fisico_list")

class TipoSensorFisicoDetailView(DetailView):
    model = TipoSensorFisico
    context_object_name = "tipo_sensor_fisico"
    template_name = "acad/TipoSensorFisico/tipo_sensor_fisico_detail.html"
    fields = ["tipo", "descricao"]

class TipoSensorFisicoDeleteView(DeleteView):
    model = TipoSensorFisico
    context_object_name = "tipo_sensor_fisico"
    template_name = "acad/TipoSensorFisico/tipo_sensor_fisico_delete.html"
    success_url = reverse_lazy("tipo_sensor_fisico_list")


class TipoSensorLogicoListView(ListView):
    model = TipoSensorLogico
    fields = ["nome", "descricao"]
    context_object_name = "tipo_sensores_logicos" 
    template_name = "acad/TipoSensorLogico/tipo_sensor_logico_list.html"

class TipoSensorLogicoCreateView(CreateView):
    model = TipoSensorLogico
    form_class = TipoSensorLogicoForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_sensor_logico" 
    template_name = "acad/TipoSensorLogico/tipo_sensor_logico_form.html"
    success_url = reverse_lazy("tipo_sensor_logico_list")

class TipoSensorLogicoUptadeView(UpdateView):
    model = TipoSensorLogico
    form_class = TipoSensorLogicoForm  # Usa o ModelForm criado
    context_object_name = "tipo_sensor_logico"
    template_name = "acad/TipoSensorLogico/tipo_sensor_logico_form.html"
    success_url = reverse_lazy("tipo_sensor_logico_list")

class TipoSensorLogicoDetailView(DetailView):
    model = TipoSensorLogico
    context_object_name = "tipo_sensor_logico"
    template_name = "acad/TipoSensorLogico/tipo_sensor_logico_detail.html"
    fields = ["tipo", "descricao"]

class TipoSensorLogicoDeleteView(DeleteView):
    model = TipoSensorLogico
    context_object_name = "tipo_sensor_logico"
    template_name = "acad/TipoSensorLogico/tipo_sensor_logico_delete.html"
    success_url = reverse_lazy("tipo_sensor_logico_list")



class TipoParametroListView(ListView):
    model = TipoParametro
    fields = ["nome", "descricao"]
    context_object_name = "tipo_parametros" 
    template_name = "acad/TipoParametro/tipo_parametro_list.html"

class TipoParametroCreateView(CreateView):
    model = TipoParametro
    form_class = TipoParametroForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_parametro" 
    template_name = "acad/TipoParametro/tipo_parametro_form.html"
    success_url = reverse_lazy("tipo_parametro_list")

class TipoParametroUptadeView(UpdateView):
    model = TipoParametro
    form_class = TipoParametroForm  # Usa o ModelForm criado
    context_object_name = "tipo_parametro"
    template_name = "acad/TipoParametro/tipo_parametro_form.html"
    success_url = reverse_lazy("tipo_parametro_list")

class TipoParametroDetailView(DetailView):
    model = TipoParametro
    context_object_name = "tipo_parametro"
    template_name = "acad/TipoParametro/tipo_parametro_detail.html"
    fields = ["tipo", "descricao"]

class TipoParametroDeleteView(DeleteView):
    model = TipoParametro
    context_object_name = "tipo_parametro"
    template_name = "acad/TipoParametro/tipo_parametro_delete.html"
    success_url = reverse_lazy("tipo_parametro_list")


class TipoPavimentoListView(ListView):
    model = TipoPavimento
    fields = ["nome", "descricao"]
    context_object_name = "tipo_pavimentos" 
    template_name = "acad/TipoPavimento/tipo_pavimento_list.html"

class TipoPavimentoCreateView(CreateView):
    model = TipoPavimento
    form_class = TipoPavimentoForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_pavimento" 
    template_name = "acad/TipoPavimento/tipo_pavimento_form.html"
    success_url = reverse_lazy("tipo_pavimento_list")

class TipoPavimentoUptadeView(UpdateView):
    model = TipoPavimento
    form_class = TipoPavimentoForm  # Usa o ModelForm criado
    context_object_name = "tipo_pavimento"
    template_name = "acad/TipoPavimento/tipo_pavimento_form.html"
    success_url = reverse_lazy("tipo_pavimento_list")

class TipoPavimentoDetailView(DetailView):
    model = TipoPavimento
    context_object_name = "tipo_pavimento"
    template_name = "acad/TipoPavimento/tipo_pavimento_detail.html"
    fields = ["tipo", "descricao"]

class TipoPavimentoDeleteView(DeleteView):
    model = TipoPavimento
    context_object_name = "tipo_pavimento"
    template_name = "acad/TipoPavimento/tipo_pavimento_delete.html"
    success_url = reverse_lazy("tipo_pavimento_list")


class TipoOrientacaoListView(ListView):
    model = TipoOrientacao
    fields = ["nome", "descricao"]
    context_object_name = "tipo_orientacoes" 
    template_name = "acad/TipoOrientacao/tipo_orientacao_list.html"

class TipoOrientacaoCreateView(CreateView):
    model = TipoOrientacao
    form_class = TipoOrientacaoForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_orientacao" 
    template_name = "acad/TipoOrientacao/tipo_orientacao_form.html"
    success_url = reverse_lazy("tipo_orientacao_list")

class TipoOrientacaoUptadeView(UpdateView):
    model = TipoOrientacao
    form_class = TipoOrientacaoForm  # Usa o ModelForm criado
    context_object_name = "tipo_orientacao"
    template_name = "acad/TipoOrientacao/tipo_orientacao_form.html"
    success_url = reverse_lazy("tipo_orientacao_list")

class TipoOrientacaoDetailView(DetailView):
    model = TipoOrientacao
    context_object_name = "tipo_orientacao"
    template_name = "acad/TipoOrientacao/tipo_orientacao_detail.html"
    fields = ["tipo", "descricao"]

class TipoOrientacaoDeleteView(DeleteView):
    model = TipoOrientacao
    context_object_name = "tipo_orientacao"
    template_name = "acad/TipoOrientacao/tipo_orientacao_delete.html"
    success_url = reverse_lazy("tipo_orientacao_list")

class TipoSalaListView(ListView):
    model = TipoSala
    context_object_name = "tipo_salas"
    template_name = "acad/TipoSala/tipo_sala_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")  # Obtém o termo digitado no campo de pesquisa
        if query:
            return TipoSala.objects.filter(nome__icontains=query)  # Filtra salas pelo nome
        return TipoSala.objects.all()  # Retorna todas as salas se não houver pesquisa

class TipoSalaCreateView(CreateView):
    model = TipoSala
    form_class = TipoSalaForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_sala" 
    template_name = "acad/TipoSala/tipo_sala_form.html"
    success_url = reverse_lazy("tipo_sala_list")

class TipoSalaUptadeView(UpdateView):
    model = TipoSala
    form_class = TipoSalaForm  # Usa o ModelForm criado
    context_object_name = "tipo_sala"
    template_name = "acad/TipoSala/tipo_sala_form.html"
    success_url = reverse_lazy("tipo_sala_list")

class TipoSalaDetailView(DetailView):
    model = TipoSala
    context_object_name = "tipo_sala"
    template_name = "acad/TipoSala/tipo_sala_detail.html"
    fields = ["tipo", "descricao"]

class TipoSalaDeleteView(DeleteView):
    model = TipoSala
    context_object_name = "tipo_sala"
    template_name = "acad/TipoSala/tipo_sala_delete.html"
    success_url = reverse_lazy("tipo_sala_list")

def relatorio_view(request):
    """Exibe o relatório com filtros aplicados"""
    # Inicializar o formulário de filtros
    form = RelatorioFiltroForm(request.GET or None)

    # Filtrar os dados
    parametros = TipoParametro.objects.all()
    if form.is_valid():
        if form.cleaned_data.get("temperatura_min"):
            parametros = parametros.filter(valor__gte=form.cleaned_data["temperatura_min"])
        if form.cleaned_data.get("temperatura_max"):
            parametros = parametros.filter(valor__lte=form.cleaned_data["temperatura_max"])
        if form.cleaned_data.get("umidade_min") or form.cleaned_data.get("umidade_max"):
            parametros = parametros.filter(nome__icontains="umidade")
        if form.cleaned_data.get("tipo_sensor"):
            tipo_sensor = form.cleaned_data["tipo_sensor"]
            if tipo_sensor == "fisico":
                parametros = parametros.filter(id_sensor_logico__isnull=True)
            elif tipo_sensor == "logico":
                parametros = parametros.filter(id_sensor_logico__isnull=False)

    # Exportar para PDF
    if "export_pdf" in request.GET:
        return gerar_pdf("acad/Relatorio/relatorio_pdf.html", {"parametros": parametros})

    return render(request, "acad/Relatorio/relatorio.html", {"form": form, "parametros": parametros})


def gerar_pdf(template_src, context_dict):
    """Gera o relatório em PDF"""
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=relatorio.pdf"
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Erro ao gerar PDF")
    return response
#edição 12/02/24
def relatorio_historico_view(request):
    form = RelatorioFiltroForm(request.GET or None)
    parametros = TipoParametro.objects.all()

    # Aplicar filtros
    if form.is_valid():
        # Filtro por data
        if form.cleaned_data.get("data_inicio"):
            parametros = parametros.filter(data__gte=form.cleaned_data["data_inicio"])
        if form.cleaned_data.get("data_fim"):
            parametros = parametros.filter(data__lte=form.cleaned_data["data_fim"])

        # Filtro por sala
        if form.cleaned_data.get("sala"):
            parametros = parametros.filter(
                id_sensor_logico__id_sensor_fisico__id_tipo__pavimento=form.cleaned_data["sala"].pavimento
            )

        # Filtro por tipo de sensor
        if form.cleaned_data.get("tipo_sensor"):
            parametros = parametros.filter(id_sensor_logico__id_tipo_sensor=form.cleaned_data["tipo_sensor"])

        # Filtro por sensor físico
        if form.cleaned_data.get("sensor_fisico"):
            parametros = parametros.filter(id_sensor_logico__id_sensor_fisico=form.cleaned_data["sensor_fisico"])
    
    # Verifica se o botão para exportar PDF foi clicado
    if request.GET.get('exportar_pdf'):
        template = get_template('acad/Relatorio/relatorio_historico_pdf.html')
        context = {
            'parametros': parametros,
            'request': request,
        }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_historico.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Erro ao gerar o PDF')
        return response

    return render(request, "acad/Relatorio/historico.html", {"form": form, "parametros": parametros})

def relatorio_valores_criticos_view(request):
    # Instanciar o formulário com os dados GET
    form = ValoresCriticosFiltroForm(request.GET or None)
    parametros_criticos = TipoParametro.objects.filter(
        Q(valor__lt=F('id_sensor_logico__id_sensor_fisico__tensao_min')) |  # Valores abaixo do limite
        Q(valor__gt=F('id_sensor_logico__id_sensor_fisico__tensao_max'))    # Valores acima do limite
    )

    # Aplicar filtros
    if form.is_valid():
        if form.cleaned_data.get("data_inicio"):
            parametros_criticos = parametros_criticos.filter(data__gte=form.cleaned_data["data_inicio"])
        if form.cleaned_data.get("data_fim"):
            parametros_criticos = parametros_criticos.filter(data__lte=form.cleaned_data["data_fim"])
        if form.cleaned_data.get("tipo_sensor"):
            parametros_criticos = parametros_criticos.filter(id_sensor_logico__id_tipo=form.cleaned_data["tipo_sensor"])

    # Agrupar e contar os sensores com mais ocorrências críticas
    parametros_criticos = parametros_criticos.values(
        'id_sensor_logico__nome'
    ).annotate(
        total_criticos=Count('id')  # Contar o número de registros críticos por sensor
    ).order_by('-total_criticos')  # Ordenar pelos sensores com mais ocorrências críticas

    return render(
        request,
        "acad/Relatorio/valores_criticos.html",
        {"form": form, "parametros_criticos": parametros_criticos}
    )


def relatorio_historico_personalizado_view(request):
    form = HistoricoPersonalizadoFiltroForm(request.GET or None)
    intervalo = request.GET.get('intervalo', '5')

    # Definindo o Model correto com base no intervalo
    if intervalo == '5':
        queryset = VWAgrupamento5Minutos.objects.all().order_by('data_hora')
    elif intervalo == '15':
        queryset = VWAgrupamento15Minutos.objects.all().order_by('data_hora')
    elif intervalo == '30':
        queryset = VWAgrupamento30Minutos.objects.all().order_by('data_hora')
    elif intervalo == '60':
        queryset = VWAgrupamento60Minutos.objects.all().order_by('data_hora')
    elif intervalo == '120':
        queryset = VWAgrupamento120Minutos.objects.all().order_by('data_hora')
    elif intervalo == '240':
        queryset = VWAgrupamento240Minutos.objects.all().order_by('data_hora')
    else:
        queryset = VWAgrupamento5Minutos.objects.all().order_by('data_hora')

    # Aplicando filtros de forma completa
    if form.is_valid():
        if form.cleaned_data.get('sala'):
            queryset = queryset.filter(sigla_sala=form.cleaned_data['sala'].sigla)
        if form.cleaned_data.get('tipo_sensor'):
            queryset = queryset.filter(tipo_sensor=form.cleaned_data['tipo_sensor'].descricao)
        if form.cleaned_data.get('data_inicio') and form.cleaned_data.get('data_fim'):
            queryset = queryset.filter(
                data_hora__range=[form.cleaned_data['data_inicio'], form.cleaned_data['data_fim']]
            )
    else:
        queryset = queryset.none()  # Se o form não for válido, retorna vazio

    # Paginação (10 registros por página)
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Preservar os parâmetros para a paginação
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    query_params = query_params.urlencode()

    context = {
        'form': form,
        'page_obj': page_obj,
        'dados': page_obj.object_list,
        'query_params': query_params
    }

    # Verifica se o parâmetro exportar_pdf foi enviado
    if request.GET.get('exportar_pdf') == "1":
        template = get_template('acad/Relatorio/historico_personalizado_pdf.html')
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_historico_personalizado.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse("Erro ao gerar o PDF")
        return response

    # Renderiza o template HTML normalmente
    return render(request, 'acad/Relatorio/historico_personalizado.html', context)


def relatorio_leituras_view(request):
    form = RelatorioLeiturasFiltroForm(request.GET or None)

    if not form.is_valid():
        leituras = LeituraSensor.objects.none()  # Retorna um QuerySet vazio se o form não for válido
    else:
        leituras = LeituraSensor.objects.select_related(
            'id_sensor_logico', 
            'id_leitura', 
            'id_leitura__id_sala'
        ).order_by('-id_leitura__data_hora')

        # Aplicar filtros se o formulário for válido
        if form.cleaned_data.get("sala"):
            leituras = leituras.filter(id_leitura__id_sala=form.cleaned_data["sala"])
        if form.cleaned_data.get("data_inicio"):
            leituras = leituras.filter(id_leitura__data_hora__date__gte=form.cleaned_data["data_inicio"])
        if form.cleaned_data.get("data_fim"):
            leituras = leituras.filter(id_leitura__data_hora__date__lte=form.cleaned_data["data_fim"])
        if form.cleaned_data.get("sensor_logico"):
            leituras = leituras.filter(id_sensor_logico=form.cleaned_data["sensor_logico"])

    # Paginação - 50 registros por página
    paginator = Paginator(leituras, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "form": form,
        "page_obj": page_obj,
        "leituras": page_obj.object_list,
        "query_params": request.GET.urlencode()
    }

    # Se o parâmetro exportar_pdf for "1", gera o PDF
    if request.GET.get('exportar_pdf') == "1":
        template = get_template('acad/Relatorio/leituras_pdf.html')
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_leituras.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse("Erro ao gerar o PDF")
        return response

    return render(request, "acad/Relatorio/leituras.html", context)

def relatorio_sensores_view(request):
    form = RelatorioSensoresFiltroForm(request.GET or None)

    # QuerySet base para aplicar os filtros
    sensores = TipoSensorLogico.objects.select_related(
        'id_sensor_fisico',
        'id_tipo_sensor'
    ).order_by('descricao')

    # Aplicar filtros somente se o formulário for válido
    if form.is_valid():
        if form.cleaned_data.get("tipo_sensor"):
            sensores = sensores.filter(id_tipo_sensor=form.cleaned_data["tipo_sensor"])
        if form.cleaned_data.get("sensor_fisico"):
            sensores = sensores.filter(id_sensor_fisico=form.cleaned_data["sensor_fisico"])
        if form.cleaned_data.get("sensor_logico"):
            sensores = sensores.filter(id=form.cleaned_data["sensor_logico"].id)
        if form.cleaned_data.get("limite_inferior"):
            sensores = sensores.filter(
                id_tipo_sensor__limite_inferior_permitido__gte=form.cleaned_data["limite_inferior"]
            )
        if form.cleaned_data.get("limite_superior"):
            sensores = sensores.filter(
                id_tipo_sensor__limite_superior_permitido__lte=form.cleaned_data["limite_superior"]
            )
    else:
        sensores = sensores.none()

    # Paginação - 50 registros por página
    paginator = Paginator(sensores, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Defina o contexto antes de usá-lo
    context = {
        "form": form,
        "page_obj": page_obj,
        "sensores": page_obj.object_list,
        "query_params": request.GET.urlencode()
    }

    # Se exportar_pdf estiver presente, gere o PDF
    if request.GET.get('exportar_pdf') == "1":
        template = get_template('acad/Relatorio/sensores_pdf.html')
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_sensores.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse("Erro ao gerar o PDF")
        return response

    # Renderiza a página HTML normalmente
    return render(request, "acad/Relatorio/sensores.html", context)