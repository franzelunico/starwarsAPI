from rest_framework import viewsets
from starwars.models import Planet, People, Rating
from starwars.serializers import (PlanetModelSerializer,
                                  PeopleModelSerializer,
                                  RatingModelSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
import swapi
from django.http import HttpResponse


class PlanetModelViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetModelSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PeopleModelViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleModelSerializer

    def retrieve(self, request, pk=None):
        instance = None
        try:
            People.objects.get(pk=pk)
            instance = People.objects.get(pk=pk)
            instance = self.get_object()
        except People.DoesNotExist:
            instance = CreatePeople()
            instance = instance.getPeople(pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class RatingModelViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
    


class CreatePeople():
    """
    pk=1 Luke
    pk=4 Darth
    pk=8 R5
    """
    def __init__(self):
        self.people = People()
        self.people_swapi = None

    # Debe retornar un objeto guardado en la base de datos
    def getPeople(self, pk):
        try:
            self.people = People.objects.get(pk=pk)
        except People.DoesNotExist:
            self.setSwapiPeople(pk)
            self.parse(pk)
        return self.people

    def setSwapiPeople(self, pk):
        self.people_swapi = swapi.get_person(pk)

    # Parsea de swapi -> People
    def parse(self, pk):
        self.people.pk = pk
        self.people.name = self.people_swapi.name
        self.people.height = self.people_swapi.height
        self.people.mass = self.people_swapi.mass
        self.people.hair_color = self.people_swapi.hair_color
        self.people.skin_color = self.people_swapi.skin_color
        self.people.eye_color = self.people_swapi.eye_color
        self.people.birth_year = self.people_swapi.birth_year
        self.people.gender = self.people_swapi.gender
        especies_qs = self.people_swapi.get_species()
        especies_items = especies_qs.items
        especie_obj = especies_items[0]
        self.people.species_name = especie_obj.name
        self.people.homeworld = self.getHomeworld()
        self.people.save()

    def getHomeworld(self):
        planet_swapi = self.people_swapi.get_homeworld()
        planet_pk = int(planet_swapi.url.split('/')[-2])

        homeworld = PlanetCreate(planet_swapi)
        homeworld = homeworld.getPlanet(planet_pk)
        return homeworld

class PlanetCreate():
    def __init__(self, planet_swapi):
        self.planet = Planet()
        self.planet_swapi = planet_swapi
        
    def parse(self, pk):
        self.planet.pk = pk
        self.planet.name = self.planet_swapi.name
        self.planet.population = self.planet_swapi.name

        residents = self.planet_swapi.residents
        self.planet.known_residents_count = len(residents)
        self.planet.save()

    def getPlanet(self, pk):
        try:
            self.planet = Planet.objects.get(pk=pk)
        except Planet.DoesNotExist:
            self.parse(pk)
        return self.planet