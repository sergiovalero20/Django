from rest_framework import generics
from myapi.models import Hero
from myapi.serializers import HeroSerializers

class HeroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers

class HeroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers