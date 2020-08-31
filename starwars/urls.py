from rest_framework import routers
from starwars.views import (PlanetModelViewSet,
                            PeopleModelViewSet,
                            RatingModelViewSet)

stroutes = routers.DefaultRouter()
stroutes.register(r'planet', PlanetModelViewSet, basename='planet')
stroutes.register(r'character', PeopleModelViewSet, basename='character')
stroutes.register(r'rating', RatingModelViewSet, basename='rating')
