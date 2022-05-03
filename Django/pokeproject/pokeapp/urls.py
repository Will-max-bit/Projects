from django.urls import path
from . import views


app_name = 'pokeapp'
urlpatterns = [
    path('load_pokemon', views.load_pokemon, name='load_pokemon'),
    path('load_vue_pokemon', views.load_vue_pokemon, name='load_vue_pokemon'),
    path('', views.vue_index, name='vue_index' ),
]
