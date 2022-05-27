from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'message': 'Hello World',
    }
    return render(request, 'pokedex_app/index.html', context)
