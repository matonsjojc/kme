from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from kme import forms

# Create your views here.
def index(request):
    context_dict = {}
    #return HttpResponse("Rango says hey there partner!")
    return render(request, 'kme/index.html', context=context_dict)

def vlagatelj_osnovni_podatki(request):
    #kle kreiraj novo Raziskavo, vezano na userprofile
    #ce je get, zacni s 1. formo (forms.form_vrstni_red["1"], sicer naprj):
    context_dict = {}
    form = forms.VlagateljForm()
    print("metoda od vlagatelj_osnovni_podatki: ", request.method)
    if request.method == 'POST':
        form = forms.VlagateljForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("validna....")
            return HttpResponseRedirect('http://127.0.0.1:8000/kme/raziskava')
        else:
            print("neki ne stima", form.errors)
    context_dict = {
        "form": form,
        }
    return render(request, 'kme/vlagatelj_osnovni_podatki.html', context=context_dict)

def raziskava(request):
    form = forms.RaziskavaForm()
    print("raziskava..., method: ", request.method)
    if request.method == 'POST':
        form = forms.RaziskavaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("validna raziskavaform..")
            return podpisnik_raziskovalec(request)
        else:
            print("raziskava_f: neki ne stima", form.errors)
    context_dict = {
        "form": form,
    }
    return render(request, 'kme/raziskava.html', context=context_dict)

def podpisnik_raziskovalec(request):
    context_dict = {
    }
    return render(request, 'kme/podpisnik_raziskovalec.html', context=context_dict)



#dodaj moznost nadaljevanja izpolnjevanja forme
