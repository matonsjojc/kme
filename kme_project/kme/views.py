from django.shortcuts import render
from django.http import HttpResponse
from kme import forms

# Create your views here.
def index(request):
    context_dict = {}
    #return HttpResponse("Rango says hey there partner!")
    return render(request, 'kme/index.html', context=context_dict)

def vlagatelj_osnovni_podatki(request):
    #kle kreiraj novo Raziskavo, vezano na userprofile
    #ce je get, zacni s 1. formo (forms.form_vrstni_red["1"], sicer naprj):
    form = forms.VlagateljForm()
    print(request.method)
    if request.method == 'POST':
        form = forms.VlagateljForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("validna....")

        else:

            print("neki ne stima", form.errors)

    context_dict = {
        "form": form,
        }

    return render(request, 'kme/vlagatelj_osnovni_podatki.html', context=context_dict)

def raziskava(request):
    context_dict = {}
    return render(request, 'kme/vloga.html', context=context_dict)

#dodaj moznost nadaljevanja izpolnjevanja forme
