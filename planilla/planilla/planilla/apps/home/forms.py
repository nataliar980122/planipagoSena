from planilla.apps.home.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class FormularioPersonas(ModelForm):
    class Meta:
        model = Contratista
        fields=[
        	"nombre", 					
			"apellido", 				
			"identificacion",			
			"telefono",				
			"correo", 				   
			"Clasificacion_persona",     
			"declarante",			   
			"pensionado", 			   
			"regimen_iva",			   
			"centro",
			"user" 	
        ]

class FormularioBancos(ModelForm):
    class Meta:
        model = Banco
        fields=[
        	"nombre_banco",
			"codigo_banco"
		] 

class Registrar_regionalForm(forms.ModelForm):
	class Meta:
		model = Regional
		fields= [
		"codigo",
		"nombre_regional"
		]

class Registrar_Banco(forms.ModelForm):
	class Meta:
		model = Banco
		fields= [
		"nombre_banco",
		"codigo_banco"
		]

class Registrar_Cuenta(forms.ModelForm):
	class Meta:
		model = Cuenta
		fields= [
		"num_cuenta",
		"tipo_cuenta",
		"banco_cuenta",
		
		]
		exclude = ("contratista")
		

class Registrar_centroForm(forms.ModelForm):
	class Meta:
		model = Centro
		fields= [
		"codigo",
		"nombre_centro",
		"regional_centro"
		]

class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave 	= forms.CharField(widget = forms.PasswordInput(render_value = False))

class registrarContratistaForm(forms.Form):
	username 		= forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email 	 		= forms.EmailField(label="Email",widget=forms.TextInput())
	password_one	= forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two 	= forms.CharField(label="Confirmar Password",widget=forms.PasswordInput(render_value=False))


	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')


	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')


	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')

class registrarSupervisorForm(forms.Form):
	nombre 			= forms.CharField(label="Nombres",widget=forms.TextInput()) 
	apellido 		= forms.CharField(label="Apellidos",widget=forms.TextInput()) 
	username 		= forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email 	 		= forms.EmailField(label="Email",widget=forms.TextInput())
	password_one	= forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two 	= forms.CharField(label="Confirmar Password",widget=forms.PasswordInput(render_value=False))


	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')


	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')


	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')
		
class DatosContratista_Form(forms.ModelForm):
	class Meta:
		model  = Contratista
		fields= [
		"nombre", 				
		"apellido" 	,		
		"identificacion",		
		"telefono"	,		
		"correo", 					
		"Clasificacion_persona" ,
		"ingresos", 	
		"declarante",			
		"pensionado" ,			
		"regimen_iva",	
		"servicios_extra",
		"objeto_embargo",
		"valor_embargo",		
		"centro",
		"tipocontratista"	
		]
		exclude = ('user')	

class add_contratista_form(forms.ModelForm):
	class Meta:
		model   = Contratista
		#Excluyo user
		exclude = {'user','status',} 

class Ordenador_pagoForm(forms.ModelForm):
	class Meta:
		model  = OrdenadorPago	

class add_actividad_form(forms.ModelForm):
	class Meta:
		model = Actividad

		exclude = {'user'}

class add_comisiones_form(forms.ModelForm):
	class Meta:
		model = Comisiones

		exclude = {'user','contrato','total'}

class add_honorario_form(forms.ModelForm):
	class Meta:
		model = Honorario	

		exclude = {'user', 'contratista', 'total'}

class ContratoForm(forms.ModelForm):
	fecha_inicio = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker'}), label='fecha_inicio')
	fecha_fin = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker2'}), label='fecha_fin')
	class Meta:
		model = Contrato
		fields= [
			"numero_contrato",			
			#"fecha_inicio",		
			#"fecha_fin",		
			"valor_total",
			"compromiso_siif",
			"forma_estimacion",
			'valor_mensual',
			"supervisor",
			"ordenador_pago"		
		]
		exclude = ('total_horas_contrato')

class Aportes_Form(forms.ModelForm):
	class Meta:
		model = Aporte
		fields= [
		"numero_plantilla",
		"tipoRiesgo_arl",
		"aporte_vpension",
		"aporte_vafc",
		"prestamo_vivienda",
		"medicina_prepagada"
					
		]
		exclude = ('ibc_aporte, salud_aporte, pension_aporte, solidaridad_aporte, arl_aporte, valor_arl, user')

class Aportes_Form2(forms.ModelForm):
	class Meta:
		model = Aporte
		fields = {'numero_plantilla'}	
		exclude = '__all__'

class ContratoForm1(forms.ModelForm):
	class Meta:
		model = Contrato
		fields= [
			"valor_mensual",
			"total_horas_contrato"
		]
		exclude = ('numero_contrato','fecha_inicio','fecha_fin','valor_total','compromiso_siif',
				   'forma_estimacion','supervisor','ordenador_pago')

class add_contrato_form(forms.ModelForm):
	fecha_inicio = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker'}), label='fecha_inicio')
	fecha_fin = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker2'}), label='fecha_fin')
	class Meta:
		model  	=  Contrato
		exclude = ('estado','contratista')


class ContratistaForm(forms.Form):
	
	username 		= forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email 	 		= forms.EmailField(label="Email",widget=forms.TextInput())
	password_one	= forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two 	= forms.CharField(label="Confirmar Password",widget=forms.PasswordInput(render_value=False))







	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')





	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')




	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')

class PagoMesForm(forms.ModelForm):
	class Meta:
		model = PagoMes
		
		fields= [
						
			"total_dias_liquidacion",		
			"fecha_inicio",		
			"fecha_fin",
			"numero_pago"
			]
		exclude = ('contrato','valor_mes','total_pagar')

class estado_contrato_form(forms.ModelForm):
	class Meta:
		model = Contrato
		fields = {'estado'}	
		exclude = '__all__' 
