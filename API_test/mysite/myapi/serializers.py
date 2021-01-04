from rest_framework import serializers
from .models import Hero

class HeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hero
        #fields = ('id','name','alias')
        fields = '__all__'