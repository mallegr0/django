from django.db import models


# Create your models here.
class Socio(models.Model):
	nroSoc = models.IntegerField(primary_key=True, null=False, blank=False)
	dni = models.IntegerField(unique=True, null=False, blank=False)
	nombre = models.CharField(max_length=15)
	apellido = models.CharField(max_length=15)
	