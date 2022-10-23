from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Movie(models.Model):
#   name = models.CharField(max_length=50)
#   image = models.ImageField(upload_to='files/covers')

class Casas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="casaspropias", null=True)
    casa_nombre= models.CharField(max_length=200)
    casa_descripcion = models.TextField(max_length=500)
    casa_direccion = models.CharField(max_length=200)
    casa_habitantes = models.IntegerField()
    casa_cuartos = models.IntegerField()
    casa_amueblada = models.BooleanField()
    casa_contacto = models.IntegerField()
    home_photo = models.ImageField(upload_to='files/covers')
    casa_aprobada = models.BooleanField(default=False)
    casa_rentada = models.BooleanField(default=False)
    casa_responsable = models.CharField(max_length=200)

    def __str__(self):
        return self.casa_nombre
