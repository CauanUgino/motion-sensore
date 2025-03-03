
#(acad/urls.py) Criada para poder fazer uma requisição na aplicação pricipal
#Necessário realizar uma chamada na setup/urls.py para que seja possível abrir os templates(ocorre uma importação da urls.py)
#edição 12/02/24
from django.urls import path
from . import views
from .views import relatorio_view
from .views import relatorio_historico_view
from .views import relatorio_valores_criticos_view
from .views import relatorio_historico_personalizado_view
from .views import relatorio_leituras_view
from acad.views import relatorio_sensores_view



urlpatterns = [
    path('grafico/', views.grafico_view, name='grafico'),
    path('grafico/dados/', views.dados_climaticos, name='dados_climaticos'),
    path('relatorios/', relatorio_view, name='relatorio'),  # Rota para os relatórios
    path('relatorios/historico/', relatorio_historico_view, name='relatorio_historico'),
    path('relatorios/valores-criticos/', relatorio_valores_criticos_view, name='relatorio_valores_criticos'),
    path('relatorios/historico-personalizado/', relatorio_historico_personalizado_view, name='relatorio_historico_personalizado'),
    path('relatorios/leituras/', relatorio_leituras_view, name='relatorio_leituras'),
    path('relatorios/sensores/', relatorio_sensores_view, name='relatorio_sensores'),


]
