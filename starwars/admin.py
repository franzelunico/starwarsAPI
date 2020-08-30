from django.contrib import admin
from starwars.models import Planet, People, Rating
# Register your models here.
admin.site.register(Planet)
admin.site.register(People)
admin.site.register(Rating)