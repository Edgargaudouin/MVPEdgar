from django.shortcuts import render, HttpResponse
from appFamilia.models import Familiar
from django.template import loader

# Create your views here.

def familia(self):
    familiar1 = Familiar( nombre = "Edgar", apellido = "Romero", parentesco = "Padre", edad = 70, fecha_nacimiento = "1952-01-24" )
    familiar1.save()

    familiar2 = Familiar( nombre = "France", apellido = "Gaudouin", parentesco = "Madre", edad = 60, fecha_nacimiento = "1962-02-15" )
    familiar2.save()

    familiar3 = Familiar( nombre = "Isamar", apellido = "Romero", parentesco = "Hermana", edad = 26, fecha_nacimiento = "1996-08-11" )
    familiar3.save()

    plantilla = loader.get_template('plantilla1.html')
    familiares = {'familiares' : [familiar1, familiar2, familiar3]}
    documento = plantilla.render(familiares)
    return HttpResponse(documento)





