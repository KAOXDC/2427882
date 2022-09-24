from django.db import models

class Marca (models.Model):
	nombre 	= models.CharField(max_length=100)

	def __str__ (self):
		return self.nombre

class Categoria (models.Model):
	nombre 	= models.CharField(max_length=100)

	def __str__ (self):
		return self.nombre

class Producto (models.Model):
	nombre 	= models.CharField(max_length=100)
	precio 	= models.IntegerField()
	stock 	= models.IntegerField()
	status 	= models.BooleanField(default=True)
	foto 	= models.ImageField(upload_to='productos', null=True, blank=True)
	marca 	= models.ForeignKey(Marca, on_delete=models.PROTECT)
	categoria = models.ManyToManyField(Categoria, null=True, blank=True)

	def __str__(self):
		return self.nombre + ' ' +str(self.id)
