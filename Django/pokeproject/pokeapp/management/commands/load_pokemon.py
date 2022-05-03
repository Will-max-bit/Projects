from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json
import os
import requests
import json
import pyperclip

#labs\django\pokeproject\pokeapp\management\commands\pokemon.json
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./pokeapp/management/commands/pokemon.json', 'r') as f:
            contents = f.read()
        Pokemon.objects.all().delete()
        data = json.loads(contents)
        for pokemon in data['pokemon']:
            number = pokemon['number']
            name = pokemon['name']
            weight = pokemon['weight']
            height = pokemon['height']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = ', '.join(pokemon['types'])
            url = pokemon['url']
            pokemon = Pokemon(number = number, name=name, height=height, weight = weight, 
                        image_front=image_front, image_back=image_back,
                        types=types, url=url)
            pokemon.save()
        





