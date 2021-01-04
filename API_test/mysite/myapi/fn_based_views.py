from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import HeroSerializers
from myapi.models import Hero
from rest_framework.response import Response

# Create your views here.
#@api_view(["GET",])
#class HeroViewSet(viewsets.ModelViewSet):
#    queryset = Hero.objects.all().order_by('name')
#    serializer_class = HeroSerializers

@api_view(["GET","POST"])
def HeroViewSet(request):
    if request.method == 'GET':
        heroes = Hero.objects.all()
        serializer = HeroSerializers(heroes, many = True)
        #return Response({
        #    'Success': True,
        #    'Message':'Get request fulfilled!!',
        #    'Data': serializer.data 
        #})
        return Response(serializer.data)

    
    if request.method == 'POST':
        serializer = HeroSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Success': True,
                'Message': 'Post request full filled!!',
                'Data': serializer.data  
            })
    return Response({
        'Success': False,
        'Message':'Invalid request',
        'Data':''
    })