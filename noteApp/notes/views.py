from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Notes
# Create your views here.

def list_notes(request):
    context ={'note_list' : Notes.objects.all()}
    #print(context['note_list'][0])
    return render(request,"notes.html",context)

def insert_notes(request:HttpRequest):
    notes = Notes(title = request.POST['title'], content = request.POST['content'])
    notes.save()
    return redirect('/')