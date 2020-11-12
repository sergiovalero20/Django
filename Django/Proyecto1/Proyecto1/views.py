from django.http import HttpResponse 
from datetime import datetime 
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
#A cada función def se le denomina view 
#Recibe un request como primer parametro y retorna un response
def mensaje(request):

#Una forma de hacerlo:

    #doc_externo = get_template('miplantilla.html')    
    #doc = doc_externo.render({"Nombre": nombre, "Apellido": apellido, "Lista":["Aprendizaje","Salud","Viajes"]})
    #return HttpResponse(doc)

#Otra forma de hacerlo es la siguiente:
    return render(request, "miplantilla.html", {"Nombre": "Sergio", "Apellido": "Valero", "Lista":["Aprendizaje","Salud","Viajes"]})

def padre(request):
    return render(request,'base.html',{"title":"Pagina Padre","footer":"Fin de la pagina"})

def h1(request):

    return render(request,'hijo.html', {"info":"Veamos el siguiente video tutorial de Django"})


