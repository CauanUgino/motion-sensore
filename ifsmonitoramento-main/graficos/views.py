from django.shortcuts import render

# Create your views here.
# views.py
#from django.http import JsonResponse
#from .models import MedicaoClimatica
'''
def dados_climaticos(request):
    # Recupera os dados do banco
    medicoes = MedicaoClimatica.objects.order_by('data_hora')
    
    # Dados para o gráfico
    labels = [medicao.data_hora.strftime('%d/%m %H:%M') for medicao in medicoes]  # Formata data/hora
    temperaturas = [medicao.temperatura for medicao in medicoes]
    umidades = [medicao.umidade for medicao in medicoes]
    sensacoes = [medicao.sensacao_termica for medicao in medicoes]
    
    return JsonResponse({
        'labels': labels,
        'temperaturas': temperaturas,
        'umidades': umidades,
        'sensacoes': sensacoes
    })
'''