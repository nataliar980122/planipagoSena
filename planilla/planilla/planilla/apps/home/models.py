from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Banco(models.Model):
	nombre_banco  = models.CharField(max_length = 100)
	codigo_banco  = models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre_banco




TIPO_ARL =(

	('I','I'),
	('II','II'),
	('III','III'),
	('IV','IV'),
	('V','V'),
)

class Aporte(models.Model):
	numero_plantilla  		= models.CharField(max_length = 100)
	ibc_aporte  			= models.CharField(max_length = 100)
	salud_aporte  			= models.IntegerField()
	pension_aporte		    = models.IntegerField()
	solidaridad_aporte 		= models.IntegerField()
	arl_aporte 				= models.CharField(max_length = 100)
	tipoRiesgo_arl  		= models.CharField(max_length = 200, choices=TIPO_ARL, default='I')
	valor_arl  				= models.IntegerField()
	aporte_vpension			= models.IntegerField(default=0)
	aporte_vafc				= models.IntegerField(default=0)
	prestamo_vivienda		= models.IntegerField(default=0)
	medicina_prepagada		= models.IntegerField(default=0)
	user 					= models.OneToOneField(User) 					
	def __unicode__ (self):
		return self.numero_plantilla



	
class Regional(models.Model):
	codigo 				= models.IntegerField()
	nombre_regional  	= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre_regional

		

class Centro(models.Model):
	codigo 				= models.IntegerField()
	nombre_centro  		= models.CharField(max_length = 100)
	regional_centro		= models.ForeignKey(Regional)
	def __unicode__ (self):
		return self.nombre_centro

class OrdenadorPago(models.Model):
	nombre 		= models.CharField(max_length = 100)
	apellido 	= models.CharField(max_length = 100)
	telefono	= models.CharField(max_length = 100)
	
	def __unicode__ (self):
		return unicode(self.nombre)+" "+ unicode(self.apellido)
				
class Supervisor(models.Model):
	nombre 			= models.CharField(max_length = 100)
	apellido 		= models.CharField(max_length = 100)
	correo			= models.CharField(max_length = 100)
	
	def __unicode__ (self):
		return unicode(self.nombre)+" "+ unicode(self.apellido)

TIPO_CUENTA =(

	('AHORROS','AHORROS'),
	('CORRIENTE','CORRIENTE'),
)
CALSIFICACION_PERSONA =(
	('Empleado','Empleado'),
	('Trabajador por cuenta propia','Trabajador por cuenta propia'),
	('Demas personas naturales','Demas personas naturales'),
)
Opcion = (
	('SI', 'SI'),
	('NO', 'NO'),

	)

tipo_contratista = (
	('Administrativo','Administrativo'),
	('Instructor','Instructor'),
	)
#contratista

class Contratista(models.Model):
	nombre 					= models.CharField(max_length = 100)
	apellido 				= models.CharField(max_length = 100)
	identificacion			= models.CharField(max_length = 100)
	telefono				= models.CharField (max_length = 100)
	correo 					= models.EmailField (max_length = 200)
	Clasificacion_persona  	= models.CharField(max_length = 200, choices=CALSIFICACION_PERSONA, default='Empleado')
	ingresos				= models.CharField(max_length = 100, choices=Opcion, default='NO')
	tipocontratista			= models.CharField(max_length = 100, choices=tipo_contratista, default='')
	declarante				= models.CharField(max_length = 100, choices=Opcion, default='NO')
	pensionado 				= models.CharField(max_length = 100, choices=Opcion, default='NO')
	regimen_iva				= models.CharField(max_length= 100, choices=Opcion, default='NO')
	servicios_extra			= models.CharField(max_length= 100, choices=Opcion, default='NO')
	objeto_embargo			= models.CharField(max_length= 100, choices=Opcion, default='NO')
	valor_embargo			= models.IntegerField(default=0)
	centro 					= models.ForeignKey(Centro)
	user 					= models.OneToOneField(User)


	def __unicode__ (self):
		return self.nombre

ESTADOS_CONTRATO =(
	('Activo','Activo'),
	('Inactivo','Inactivo'),
	('Suspendido','Suspendido'),
)
Forma_Estimacion =(
	('Por Periodo(MES)','Por Periodo(MES)'),
	('Por Hora',('Por Hora'))
	)

class Contrato(models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Contrato/%s%s"%(self.nombre, str(filename))
		return ruta
		
	numero_contrato			= models.CharField(max_length = 100)
	fecha_inicio			= models.DateField(max_length = 100)
	fecha_fin				= models.DateField(max_length = 100)
	valor_total				= models.IntegerField()
	valor_mensual			= models.IntegerField()
	compromiso_siif			= models.IntegerField()
	forma_estimacion		= models.CharField(max_length = 100, choices=Forma_Estimacion, default='Por Periodo(MES)')
	supervisor 				= models.ForeignKey(Supervisor)
	ordenador_pago 			= models.ForeignKey(OrdenadorPago)
	total_horas_contrato 	= models.IntegerField()
	contratista 			= models.OneToOneField(Contratista)
	estado 					= models.CharField(max_length=100, choices=ESTADOS_CONTRATO, default='Activo')
	

	def __unicode__ (self):
		return self.numero_contrato

class Comisiones(models.Model):
	numero_comision = models.CharField(max_length = 200)
	valor_comision	= models.IntegerField()
	valor_retenido	= models.IntegerField()
	total 			= models.IntegerField()
	contrato 		= models.ForeignKey(Contrato)
	user 			= models.ForeignKey(User)
	def __unicode__ (self):
		return self.numero_comision


class Embargo(models.Model):
	codigo 		=models.CharField(max_length = 200)
	objeto 		=models.CharField(max_length = 200)
	valor 		= models.IntegerField()
	contrato 	= models.ForeignKey(Contrato)

	def __unicode__ (self):
		return self.codigo
		
class PagoMes(models.Model):
	valor_mes				= models.IntegerField()
	total_dias_liquidacion	= models.IntegerField()
	fecha_inicio			= models.DateField(max_length = 100)
	fecha_fin				= models.DateField(max_length = 100)
	saldo_anterior			= models.IntegerField()
	saldo_nuevo				= models.IntegerField()
	total_pagar				= models.IntegerField()
	numero_pago				= models.CharField(max_length = 100)
	contrato				= models.ForeignKey(Contrato)
	
	
	def __unicode__ (self):
		return str( self.saldo_anterior)

class PagoHora(models.Model):
	numero_horas	= models.IntegerField()
	valor_hora		= models.IntegerField()
	valor_pagar		= models.IntegerField()
	contrato 		= models.ForeignKey(Contrato)
	
	def __unicode__ (self):
		return "valor  Hora "+unicode(self.valor_hora)+"valor  total "+unicode(self.valor_pagar)#+str(self.valor_pagar)

class Cuenta(models.Model):
	num_cuenta  		= models.IntegerField()
	tipo_cuenta  		= models.CharField(max_length = 200, choices=TIPO_CUENTA, default='CORRIENTE')
	banco_cuenta 		= models.ForeignKey(Banco)
	contratista 		= models.ForeignKey(Contratista)
	def __unicode__ (self):
		return self.tipo_cuenta


class Actividad(models.Model):

	numero_ficha 			= models.IntegerField(blank = True)
	descripcion_actividad 	= models.CharField(max_length = 200)
	resultado  				= models.CharField(max_length = 200)
	horas_laboradas			= models.IntegerField(blank = True)
	fecha_actividad 		= models.DateField(auto_now = True)
	user 					= models.ForeignKey(User)
	def __unicode__ (self):
		return self.numero_ficha

		
class Honorario(models.Model):
	concepto 			= models.CharField(max_length = 200)
	valor_hora			= models.IntegerField()
	valor_retenido		= models.IntegerField()
	total 		  		= models.IntegerField()
	user 				= models.ForeignKey(User)
	def __unicode__ (self):
		return self.concepto


class user_profile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return ruta

	user 		=	models.OneToOneField(User)
	photo		=	models.ImageField(upload_to=url)
	telefono	=	models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username

	