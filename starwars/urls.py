from rest_framework import routers
from django.urls import path
from starwars.views import (PlanetModelViewSet,
                            PeopleModelViewSet,
                            RatingModelViewSet)

stroutes = routers.DefaultRouter()
stroutes.register(r'planet', PlanetModelViewSet, basename='planet')
stroutes.register(r'character', PeopleModelViewSet, basename='character')
stroutes.register(r'rating', RatingModelViewSet, basename='rating')



#urlpatterns = [
#    path('character/', personaje_list),
#    path('character/<int:pk>/', personaje_detail),
#]