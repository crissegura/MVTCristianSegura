from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiares

def familiar(request):
    familiar1 = Familiares(nombre='Juan Segura',edad=34)
    familiar1.save()
    familiar2 = Familiares(nombre='Roman Segura',edad=24)
    familiar2.save()
    familiar3 = Familiares(nombre='Martin Segura',edad=14)
    familiar3.save()
    texto1 = f"Familiar: {familiar1.nombre} Edad: {familiar1.edad} "
    texto2 = f"Familiar: {familiar2.nombre} Edad:{familiar2.edad} "
    texto3 = f"Familiar: {familiar3.nombre} Edad: {familiar3.edad} "
    return HttpResponse(texto1+' // '+texto2+' // '+texto3) 

