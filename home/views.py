from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def reseta_senha(request):
    return render(request,'reset_senha.html')

def cadastro_usuario(request):
    return render(request,'index_cadastro.html')