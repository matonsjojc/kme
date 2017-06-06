from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {}
    #return HttpResponse("Rango says hey there partner!")
    return render(request, 'kme/index.html', context=context_dict)

def nova_vloga(request):
    context_dict = {}
    return render(request, 'kme/vloga.html')




#dodaj moznost nadaljevanja izpolnjevanja forme
