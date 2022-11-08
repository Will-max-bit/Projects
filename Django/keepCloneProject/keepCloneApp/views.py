from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
def index(request):
    notes = Notes.objects.all()
    note_data = []
    for note in notes:
        note_data.append({
            'title': note.title,
            'note_body': note.note_body,
        })
    return JsonResponse({'notes': note_data})
    return HttpResponse('hello World')