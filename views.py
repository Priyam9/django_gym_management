from django.shortcuts import render,redirect
from .models import bodyflex_memebers
from .forms import bodyflex_form

def save(request):
    if request.method == "POST":
        data = bodyflex_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect("/")
    else:
        ff = bodyflex_form()
        return render(request, 'show.html', {"form": ff})

def displaydata(request):
    data = bodyflex_memebers.objects.all()
    return render(request, 'display.html', {"res": data})

def edit(request,id):
    data = bodyflex_memebers.objects.get(id=id)
    return render(request, 'edit.html', {'res': data})

def updatedata(request,id):
    mem = bodyflex_memebers.objects.all(id=id)
    data = bodyflex_form(request.POST, instance=mem)
    if data.is_valid():
        data.save()
        return redirect('/display')

def deletedata(request,id):
    data = bodyflex_memebers.objects.get(id=id)
    data.delete()
    return redirect('/display')