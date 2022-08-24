from django.shortcuts import render, HttpResponse
from appFamilia.models import Familiar
from django.template import Template, Context
# Create your views here.

def familia(self):
    familiar1 = Familiar( nombre = "Edgar", apellido = "Romero", parentezco = "Padre", edad = 70, fecha_nacimiento = "1952-01-24" )
    familiar1.save()

    familiar2 = Familiar( nombre = "France", apellido = "Gaudouin", parentezco = "Madre", edad = 60, fecha_nacimiento = "1962-02-15" )
    familiar2.save()

    familiar3 = Familiar( nombre = "Isamar", apellido = "Romero", parentezco = "Hermana", edad = 26, fecha_nacimiento = "1996-08-11" )
    familiar3.save()

    diccionario = {"familiares": [familiar1, familiar2, familiar3]}
    miHtml = open('C:/Users/Edgar/Desktop/MVPEdgar/Proyecto/plantillas/plantilla1.html')
    plantilla = Template(miHtml.read())
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)



