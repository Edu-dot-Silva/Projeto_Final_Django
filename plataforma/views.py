from django.shortcuts import render

from home import views

def plataforma(request):
    return render(request,'index_plataforma.html')
