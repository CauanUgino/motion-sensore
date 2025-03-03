"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include # campo para adicionar do código principal
#from django.views.generic import TemplateView
from django.urls import path
from django.contrib import admin
from acad.views import (
    TipoSensorCreateView,
    TipoSensorDeleteView,
    TipoSensorDetailView,
    TipoSensorListView,
    TipoSensorUptadeView,
    TipoSensorFisicoListView,
    TipoSensorFisicoCreateView,
    TipoSensorFisicoUptadeView,
    TipoSensorFisicoDeleteView,
    TipoSensorFisicoDetailView,
    TipoSensorLogicoListView,
    TipoSensorLogicoCreateView,
    TipoSensorLogicoUptadeView,
    TipoSensorLogicoDeleteView,
    TipoSensorLogicoDetailView,
    TipoParametroListView,
    TipoParametroCreateView,
    TipoParametroUptadeView,
    TipoParametroDeleteView,
    TipoParametroDetailView,
    TipoPavimentoListView,
    TipoPavimentoCreateView,
    TipoPavimentoUptadeView,
    TipoPavimentoDeleteView,
    TipoPavimentoDetailView,
    TipoOrientacaoListView,
    TipoOrientacaoCreateView,
    TipoOrientacaoUptadeView,
    TipoOrientacaoDeleteView,
    TipoOrientacaoDetailView,
    TipoSalaListView,
    TipoSalaCreateView,
    TipoSalaUptadeView,
    TipoSalaDeleteView,
    TipoSalaDetailView,
    home
)
#edição 12/02/24
urlpatterns = [ path('admin/', admin.site.urls),
              
path('', include('acad.urls')),  # campo para adicionar do código principal
path('acad/', include('acad.urls')), 
path('', home, name="home"),

path("sensorfisico/",   TipoSensorFisicoListView.as_view(), name="tipo_sensor_fisico_list"),
path("sensorfisico/create", TipoSensorFisicoCreateView.as_view(), name="tipo_sensor_fisico_create"),
path("sensorfisico/update/<int:pk>", TipoSensorFisicoUptadeView.as_view(), name="tipo_sensor_fisico_update"),
path("sensorfisico/delete/<int:pk>", TipoSensorFisicoDeleteView.as_view(), name="tipo_sensor_fisico_delete"),
path("sensorfisico/detail/<int:pk>", TipoSensorFisicoDetailView.as_view(), name="tipo_sensor_fisico_detail"),

path("sensor/",   TipoSensorListView.as_view(), name="tipo_sensor_list"),
path("sensor/create", TipoSensorCreateView.as_view(), name="tipo_sensor_create"),
path("sensor/update/<int:pk>", TipoSensorUptadeView.as_view(), name="tipo_sensor_update"),
path("sensor/delete/<int:pk>", TipoSensorDeleteView.as_view(), name="tipo_sensor_delete"),
path("sensor/detail/<int:pk>", TipoSensorDetailView.as_view(), name="tipo_sensor_detail"),


path("sensorlogico/",   TipoSensorLogicoListView.as_view(), name="tipo_sensor_logico_list"),
path("sensorlogico/create", TipoSensorLogicoCreateView.as_view(), name="tipo_sensor_logico_create"),
path("sensorlogico/update/<int:pk>", TipoSensorLogicoUptadeView.as_view(), name="tipo_sensor_logico_update"),
path("sensorlogico/delete/<int:pk>", TipoSensorLogicoDeleteView.as_view(), name="tipo_sensor_logico_delete"),
path("sensorlogico/detail/<int:pk>", TipoSensorLogicoDetailView.as_view(), name="tipo_sensor_logico_detail"),

path("parametro/",   TipoParametroListView.as_view(), name="tipo_parametro_list"),
path("parametro/create", TipoParametroCreateView.as_view(), name="tipo_parametro_create"),
path("parametro/update/<int:pk>", TipoParametroUptadeView.as_view(), name="tipo_parametro_update"),
path("parametro/delete/<int:pk>", TipoParametroDeleteView.as_view(), name="tipo_parametro_delete"),
path("parametro/detail/<int:pk>", TipoParametroDetailView.as_view(), name="tipo_parametro_detail"),

path("pavimento/",   TipoPavimentoListView.as_view(), name="tipo_pavimento_list"),
path("pavimento/create", TipoPavimentoCreateView.as_view(), name="tipo_pavimento_create"),
path("pavimento/update/<int:pk>", TipoPavimentoUptadeView.as_view(), name="tipo_pavimento_update"),
path("pavimento/delete/<int:pk>", TipoPavimentoDeleteView.as_view(), name="tipo_pavimento_delete"),
path("pavimento/detail/<int:pk>", TipoPavimentoDetailView.as_view(), name="tipo_pavimento_detail"),

path("orientacao/",   TipoOrientacaoListView.as_view(), name="tipo_orientacao_list"),
path("orientacao/create", TipoOrientacaoCreateView.as_view(), name="tipo_orientacao_create"),
path("orientacao/update/<int:pk>", TipoOrientacaoUptadeView.as_view(), name="tipo_orientacao_update"),
path("orientacao/delete/<int:pk>", TipoOrientacaoDeleteView.as_view(), name="tipo_orientacao_delete"),
path("orientacao/detail/<int:pk>", TipoOrientacaoDetailView.as_view(), name="tipo_orientacao_detail"),

path("sala/",   TipoSalaListView.as_view(), name="tipo_sala_list"),
path("sala/create", TipoSalaCreateView.as_view(), name="tipo_sala_create"),
path("sala/update/<int:pk>", TipoSalaUptadeView.as_view(), name="tipo_sala_update"),
path("sala/delete/<int:pk>", TipoSalaDeleteView.as_view(), name="tipo_sala_delete"),
path("sala/detail/<int:pk>", TipoSalaDetailView.as_view(), name="tipo_sala_detail"),








]

