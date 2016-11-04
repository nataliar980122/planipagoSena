from django.conf.urls.defaults import patterns, url
from .views import *
from .models import *
from planilla.apps.home.models import Contratista
from planilla.apps.home.forms import *


urlpatterns = patterns('planilla.apps.home.views',

	url(r'^ver/planilla/$','mostrarTabla', name='vista_tabla'),

	#LUIS ENRIQUE MORA, ALEX ARMANDO CAMPO VILLANO
	url(r'^descargar/$', 'llenarDatos_view', name='vista_descargar'),


	url(r'^acerca/$','acerca_view', name = 'vista_acerca'),
	url(r'^$','index_view', name = 'vista_principal'),
	url(r'^contrato/$', 'contrato_view', name ='vista_contrato'),
	url(r'^registro/$','register_view',name='vista_registro'),
	url(r'^datoscontratista/$','datoscontratista_view',name='vista_datoscontratista'),
	url(r'^login/$','login_view', name = 'vista_login'),
	url(r'^logout/$','logout_view', name = 'vista_logout'),
	url(r'^registrarusuario/$','registrarContratista_view', name = 'vista_registrarusuario'),
	url(r'^registrarcontratista/$','contratista_view', name = 'vista_contratista'),
	#url(r'^buscar/$', busqueda_view.as_view(), name ='vista_buscar'),
	#anyi
	url(r'^comisiones/$','add_comisiones_view', name = 'vista_agregar_comisiones'),
	url(r'^comilista/page/(?P<pagina>.*)/$', 'comilista_view', name = 'vista_comilista'),
	url(r'^comisiones/(?P<id_co>.*)/$', 'ver_comisiones_view', name= 'vista_ver_comisiones'),
	url(r'^edit/comilista/(?P<id_co>.*)/$', 'edit_comisiones_view', name= 'vista_editar_comisiones'),
	url(r'^del/comilista/(?P<id_co>.*)/$', 'del_comisiones_view', name= 'vista_eliminar_comisiones'),

	# honorario

	url(r'^honorario/$','add_honorario_view', name = 'vista_agregar_honorario'),
	url(r'^honoralista/page/(?P<pagina>.*)/$', 'honoralista_view', name = 'vista_honoralista'),
	url(r'^honorario/(?P<id_hono>.*)/$', 'ver_honorario_view', name= 'vista_ver_honorario'),
	url(r'^edit/honoralista/(?P<id_hono>.*)/$', 'edit_honorario_view', name= 'vista_editar_honorario'),
	url(r'^del/honoralista/(?P<id_hono>.*)/$', 'del_honorario_view', name= 'vista_eliminar_honorario'),
	
	#actividad
	url(r'^actividad/$','add_actividad_view', name = 'vista_agregar_actividad'),
	url(r'^actividades/page/(?P<pagina>.*)/$', 'actividades_view', name = 'vista_actividades'),
	url(r'^actividad/(?P<id_acti>.*)/$', 'ver_actividad_view', name= 'vista_ver_actividad'),
	url(r'^edit/actividad/(?P<id_acti>.*)/$', 'edit_actividad_view', name= 'vista_editar_actividad'),
	url(r'^del/actividad/(?P<id_acti>.*)/$', 'del_actividad_view', name= 'vista_eliminar_actividad'),


	url(r'^edit/contrato/(?P<id_cont>.*)/$', 'edit_contrato_view', name='vista_editar_contrato'),
	url(r'^agregar/contrato/$','add_contrato_view',name = 'vista_agregar_contrato'),
	url(r'^contrato/page/(?P<pagina>.*)/$','contrato_view', name = 'vista_contrato'), 
	

	# felipe
	url(r'^agregar/regional/$','agregarRegional_View',name = 'vista_agregarRegional'),
	url(r'^agregar/centro/$','agregarCentro_View',name = 'vista_agregarCentro'),
	url(r'^agregar/banco/$','agregarBanco_View',name = 'vista_agregarBanco'),
	url(r'^agregar/cuenta/$','agregarCuenta_View',name = 'vista_agregarCuenta'),
	
    #daniel
    url(r'^planilla/(?P<id_plani>.*)/$', 'single_planilla_view', name= 'vista_single_planilla'),
	url(r'^planilla/$','planilla_view', name = 'vista_planilla'),
	#chilitoandres
	
	url(r'^demo/$','demo_view',name = 'vista_demo'),

	#ELIANA
	url(r'^add/contratista/$','add_contratista_view',name = 'vista_agregar_contratista'),
	url(r'^contratista/(?P<id_contratista>.*)/$', 'single_contratista_view', name = 'vista_single_contratista'),
	url(r'^contratistas/$', 'contratistas_view', name = 'vista_contratistas'), #Listar Contratistas
	url(r'^edit/contratista/(?P<id_contratista>.*)/$', 'edit_contratista_view', name = 'vista_editar_contratista'),
	url(r'^ver/contratista/$', 'listacontratista_view', name = 'vista_listacontratista'),

	#APortes
	url(r'^agregar/aportes/$','aportes_view',name = 'vista_aportes'),
	url(r'^ver/aportes/$', 'listaaportes_view', name = 'vista_listaaportes'),
	url(r'^edit/aporte/(?P<id_aporte>.*)/$', 'edit_aporte_view', name = 'vista_editar_aporte'),
	url(r'^edit/numeroplantilla/$', 'edit_numeroplantilla_view', name = 'vista_editar_numeroplantilla'),



	url(r'^estado/contrato/(?P<id_contrato>.*)/$', 'estado_contrato_view', name = 'vista_editar_estado_contrato'),
	#usuarios
	url(r'^gestion/$','supervisor_view',name = 'vista_supervisor'),
	url(r'^registrar/supervisor/$','registrarsupervisor_view',name = 'vista_registrarSupervisor'),
	url(r'^registrar/ordenador/$','add_ordenador_view',name = 'vista_registrarOrdenador'),
	url(r'^pagomes/$','pagoMes_view',name = 'vista_pagomes'),
	
)