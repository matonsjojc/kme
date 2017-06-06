from django.shortcuts import render
from django.http import HttpResponse
from kme import forms

# Create your views here.
def index(request):
    context_dict = {}
    #return HttpResponse("Rango says hey there partner!")
    return render(request, 'kme/index.html', context=context_dict)

def nova_vloga(request):
    context_dict = {}
    #kle kreiraj novo Raziskavo, vezano na userprofile
    #zacni s 1. formo (forms.form_vrstni_red["1"]):
    form = forms.form_vrstni_red["2"]
    context_dict["form"] = form
    return render(request, 'kme/vloga.html', context=context_dict)

def izpolnjevanje(request):
    context_dict = {}
    return render(request, 'kme/vloga.html', context=context_dict)

#dodaj moznost nadaljevanja izpolnjevanja forme
