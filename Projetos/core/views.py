from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {
        "titulo":"Faculdade Impacta"
    }
    return render(request, "index.html", context)

