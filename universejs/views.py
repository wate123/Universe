from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Planet, Star
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
import pickle


class Home(TemplateView):
    template_name = 'universejs/index.html'

    def get_planet(self):
        planet_data = {}
        for planet in Planet.objects.all():
            planet_data[planet.name] = Planet.objects.filter(name=planet.name).values()[0]
        return json.dumps(planet_data, cls=DjangoJSONEncoder)

    def planet_names(self):
        names = list(Planet.objects.values_list("name"))
        return json.dumps(names, cls=DjangoJSONEncoder)

