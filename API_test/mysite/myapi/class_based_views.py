from rest_framework.views import APIView
from myapi.models import Hero
from myapi.serializers import HeroSerializers
from rest_framework.response import Response

class HeroAPIView(APIView):
    
    def get(self, request):
        hero = Hero.objects.all()
        serializer = HeroSerializers(hero, many = True)
        return Response({
            'Success': True,
            'Data': serializer.data
        })

    def post(self, request):
        if request.data.get('name') != '':
            serializer = HeroSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response ({
                    'Success': True,
                    'Data':serializer.data
                })
    
    def put(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            hero = Hero.objects.get(pk = request.data.get('id'))
            if hero:
                serializer = HeroSerializers(hero, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'Success':True,
                        'Message': 'Updated!!',
                        'Data': serializer.data
                    })
        return Response({
            'Success': False,
            'Message':'Not Found',
        })

    def delete(self, request):
        if request.data.get('id') is not None:
            hero = Hero.objects.get(pk = request.data.get('id'))
            if hero:
                hero.delete()
                return Response({
                    'Success': True,
                    'Message': 'Deleted super heroes' 
                })
        return Response ({
            'Success': False,
            'Message': 'Nof found'
        })
