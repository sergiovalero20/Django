from rest_framework import viewsets
from myapi.models import Hero
from myapi.serializers import HeroSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class HeroViewSet(viewsets.ViewSet):
    #Return a list of heroes
    def list(self, request):
        queryset = Hero.objects.all()
        serializer = HeroSerializers(queryset, many = True)
        return Response(serializer.data)
    
    #Return one hero 
    def retrieve(self, request, pk=None):
        queryset = Hero.objects.all()
        if pk is not None:
            hero = get_object_or_404(queryset, pk = pk)
            serializer = HeroSerializers(hero)
            return Response(serializer.data)
        