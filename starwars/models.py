from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Planet(models.Model):
    name = models.CharField(max_length=255, unique=True)
    population = models.CharField(max_length=255, default='0')
    known_residents_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class People(models.Model):
    name = models.CharField(max_length=255, unique=True)
    height = models.CharField(max_length=255, default='')
    mass = models.CharField(max_length=255, default='')
    hair_color = models.CharField(max_length=255, default='')
    skin_color = models.CharField(max_length=255, default='')
    eye_color = models.CharField(max_length=255, default='')
    birth_year = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='')
    species_name = models.CharField(max_length=255, default='')
    homeworld = models.ForeignKey(Planet,
                                  null=True,
                                  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    personaje = models.ForeignKey(People,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  related_name='ratings')
    
    def __str__(self):
        return str(self.rating)
