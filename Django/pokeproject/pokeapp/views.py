from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, Http404, HttpResponse
from .models import Pokemon
from django.http import HttpResponse, JsonResponse
import json
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.db.models import Q
# Create your views here.





# using built in Django pagination
def load_pokemon(request):
    # return HttpResponse('ok')

    pokemon_all = Pokemon.objects.all()
    paginator = Paginator(pokemon_all, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pokeapp/index.html', {'pokemon_all': pokemon_all, 'page_obj': page_obj })
# ################################ Vue JS rendering below###################################

def vue_index(request):
    return render(request, 'pokeapp/vue_index.html')


def load_vue_pokemon(request):
    # Getting the pokemon out of database
    list_pokemon = Pokemon.objects.all()
    num_pages = 1
    total = list_pokemon.count()
    # search through database
    if 'search' in request.GET:
        search = request.GET['search']
        list_pokemon = list_pokemon.filter(Q(name__icontains=search)| Q(types__icontains=search))
# determining pagination 
    if 'page' in request.GET:
        page = request.GET['page']
        paginator = Paginator(list_pokemon, 20)
        list_pokemon = paginator.page(page)
        num_pages = paginator.num_pages
# grabbing poke data, assigning to a list then including data with pagination in Json response
    list_pokemon_data = []
    for pokemon in list_pokemon:
        list_pokemon_data.append({
            'name': pokemon.name,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'type': pokemon.types,
            'image_front': pokemon.image_front,
            'image_back': pokemon.image_back,
            'url': pokemon.url,

        })
    return JsonResponse({'list_pokemon': list_pokemon_data, 'num_pages': num_pages, 'total': total})