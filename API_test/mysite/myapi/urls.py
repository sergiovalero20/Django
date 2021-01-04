from django.urls import include, path
from rest_framework import routers
from myapi.fn_based_views import HeroViewSet 
from myapi.class_based_views import HeroAPIView
from myapi.generic_api_views import HeroListCreateAPIView, HeroRetrieveUpdateDestroyAPIView
from myapi.viewset_api_view import HeroViewSet
#router = routers.DefaultRouter()
#router.register(r'heroes', views.HeroViewSet)

#urlpatterns = [
#    path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls',
#namespace='rest_framework'))
#]

hero_list = HeroViewSet.as_view({
    'get':'list'
})

hero_detail = HeroViewSet.as_view({
    'get':'retrieve'
})
urlpatterns = [
    path('', HeroViewSet),
    path('apiviews/', HeroAPIView.as_view()),
    path('generics/', HeroListCreateAPIView.as_view()),
    path('generics/<int:pk>/', HeroRetrieveUpdateDestroyAPIView.as_view()),
    path('viewsets/', hero_list, name = 'hero-list'),
    path('viewsets/<int:pk>/', hero_detail, name = 'hero-detail'),
]