from rest_framework import serializers
from starwars.models import Planet, People, Rating
from django.db.models import Avg
from rest_framework.decorators import action


class PlanetModelSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Planet
        fields = '__all__'


class PeopleModelSerializer(serializers.ModelSerializer):
    homeworld = PlanetModelSerializer(read_only=True)
    class Meta:
        many=True
        model = People
        fields = ['id', 'name', 'height', 'mass', 'hair_color',
                  'skin_color', 'eye_color', 'birth_year', 'gender',
                  'species_name', 'homeworld', 'rating', 'max',]
        read_only_fields = ['rating', 'max']

class RatingModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        many=True
        model = Rating
        fields = ['id', 'rating', 'personaje']

    def validate_rating(self, value):
        if (not 0 < value < 6):
            raise serializers.ValidationError('El rating debe estar entre 1 y 5')
        return value




