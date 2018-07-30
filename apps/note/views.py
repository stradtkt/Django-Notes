# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,  redirect
from .models import Note
# Create your views here.
def index(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, 'note/index.html', context)

def process_note(request):
    note = request.POST['note']
    Note.objects.create(note=note)
    messages.success(request, 'Note created')
    return redirect('/')