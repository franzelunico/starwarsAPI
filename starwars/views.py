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
        


class RatingModelViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
    




