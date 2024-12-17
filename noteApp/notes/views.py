from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Notes
# Create your views here.

def list_notes(request):
    context ={'note_list' : Notes.objects.all()};
    print(context)
    return render(request,"notes.html",context);

def insert_notes(request:HttpRequest):
    myNote = Notes(title = request.POST['title'], content = request.POST['content'])
    myNote.save()
    return redirect('/')