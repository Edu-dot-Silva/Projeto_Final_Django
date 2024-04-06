from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html')

def reseta_senha(request):
    return render(request,'reset_senha.html')

def cadastro_usuario(request):
    return render(request,'index_cadastro.html')

def plataforma (request):
    return render(request,'index_plataforma.html')

def criar_usuario(request):
    nome = request.POST['nome']
    email = request.POST['email']
    senha = request.POST['senha']
    
    usuario = User.objects.create(username = nome,email = email,password = senha)
    
    usuario.save()
    
    return redirect('home')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email = email).values_list('username',flat=True).get()
            
            usuario = authenticate(username=nome, password=senha)
            
            if usuario is not None:
                print("logou")
                return render(request,'index_plataforma.html')
            
        return render(request,'index.html')
        
        
            
    
    