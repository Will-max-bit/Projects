from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .models import Notes

CURRENT_TIME = timezone.now()
def index(request) -> HttpResponse:
    return render(request, 'keepCloneApp/index.html')

def db_notes(request) -> JsonResponse:
    saved_notes = Notes.objects.all()
    note_data = []
    for note in saved_notes:
        note_data.append({
            'title': note.title,
            'note_body': note.note_body,
            'id': note.id,
        })
    return JsonResponse({'notes': note_data})

def save_note(request) -> HttpResponse:
    note = Notes(
        title = request.POST['title'],
        note_body = request.POST['note_body'],
        created_date = CURRENT_TIME
    )
    note.save()
    return HttpResponse('good')

def edit_note(request) -> HttpResponse:
    note_id = int(request.POST.get('id'))
    note = get_object_or_404(Notes,id=note_id)
    note.title = request.POST['title']
    note.note_body = request.POST['body']
    note.created_date = CURRENT_TIME
    note.save()
    return HttpResponse('edited')

def delete_note(request) -> HttpResponse:
    deleted_note_id = int(request.POST.get('id'))
    deleted_note = get_object_or_404(Notes,id = deleted_note_id)
    deleted_note.delete()
    return HttpResponse('deleted')