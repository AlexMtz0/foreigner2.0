from django import forms

class CrearCasa(forms.Form):
    casa_nombre = forms.CharField(label="Titulo de la casa", max_length=200)
    casa_descripcion = forms.CharField(label="Descripción", max_length=500)
    casa_direccion = forms.CharField(label="Dirección", max_length=200)
    casa_habitantes = forms.IntegerField(label="Máximos habitantes")
    casa_cuartos = forms.IntegerField(label="Cantidad de cuartos disponibles")
    casa_amueblada = forms.BooleanField(label="Amueblada")
    casa_contacto = forms.IntegerField(label="Número de contacto")
    casa_responsable = forms.CharField(label="Nombre del propietario", max_length=200)

class Foto(forms.Form):
    home_photo = forms.ImageField()