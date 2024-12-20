from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Notes
# Create your views here.

def list_notes(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        notes = Notes.objects.filter(user_id=user_id)
        context = {'note_list': notes}
        return render(request, "notes.html", context)
    return HttpResponse("login first")

def insert_notes(request:HttpRequest):
    notes = Notes(title = request.POST['title'], content = request.POST['content'])
    notes.save()
    return redirect('/')