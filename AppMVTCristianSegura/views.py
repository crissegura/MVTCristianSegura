from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiares

def familiar(request):
    familiar1 = Familiares(nombre='Juan Segura',edad=34,nacimiento='02/10/88')
    familiar1.save()
    familiar2 = Familiares(nombre='Roman Segura',edad=24,nacimiento='05/06/98')
    familiar2.save()
    familiar3 = Familiares(nombre='Martin Segura',edad=14,nacimiento='10/11/08')
    familiar3.save()
    texto1 = f"Familiar: {familiar1.nombre} Edad: {familiar1.edad} Fecha de nacimiento: {familiar1.nacimiento}  "
    texto2 = f"Familiar: {familiar2.nombre} Edad:{familiar2.edad} Fecha de nacimiento: {familiar2.nacimiento} "
    texto3 = f"Familiar: {familiar3.nombre} Edad: {familiar3.edad} Fecha de nacimiento: {familiar3.nacimiento} "
    return HttpResponse(texto1+' // '+texto2+' // '+texto3) 

