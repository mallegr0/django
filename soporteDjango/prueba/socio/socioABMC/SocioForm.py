from django import forms
from socioABMC.models import Socio


class SocioForm(forms.ModelForm):

	class Meta:

		model = Socio

		fields = ['dni', 'nombre', 'apellido']

		labels = {
			'dni': 'DNI Socio',
			'nombre': 'Nombre Socio',
			'apellido': 'Apellido Socio',
		}

		widgets = {
			'dni': forms.TextInput(attrs={'required':True}),
			'nombre': forms.TextInput(attrs={'min_length':3}),
			'apellido': forms.TextInput(attrs={'min_length':3}),
		}

	def clean_nombre(self):
		nom = self.cleaned_data.get('nombre')
		if(len(nom) <3 or len(nom)>15):
			raise forms.ValidationError('longitud del nombre es incorrecto, tiene que tener entre 3 y 15 caracteres')
		return nom

	def clean_dni(self):
		doc = self.cleaned_data.get('dni')
		print(doc)
		obj = Socio.objects.filter(dni=doc).count()
		if obj > 0:
			raise forms.ValidationError('El Dni ya existe')
		return doc