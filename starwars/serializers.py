from rest_framework import serializers
from starwars.models import Planet, People, Rating
from django.db.models import Avg


class PlanetModelSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Planet
        fields = '__all__'


class PeopleModelSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True, read_only=True)
    # ratings = Rating.objects.all().aggregate(Avg('rating'))
    homeworld = PlanetModelSerializer(read_only=True)
    class Meta:
        many=True
        model = People
        fields = '__all__'


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


