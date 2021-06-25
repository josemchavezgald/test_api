from django.db import models

# Create your models here.

class Tablero(models.Model):

	largo = models.IntegerField(null=True)
	ancho = models.IntegerField(null=True)
	espesor = models.FloatField(null=True)

class Patas(models.Model):

	largo = models.FloatField(null=True)
	ancho = models.FloatField(null=True)
	espesor = models.FloatField(null=True)
	cantidad = models.IntegerField(null=True)

class Tornillo(models.Model):

	largo = models.FloatField(null=True)
	diametro = models.FloatField(null=True)
	cantidad = models.IntegerField(null=True)

class Mesa(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
	patas = models.ForeignKey(Patas, on_delete=models.CASCADE)
	tornillos = models.ForeignKey(Tornillo,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre
