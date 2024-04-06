from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='home'),
    
    path('reset_senha',views.reseta_senha,name='reset_senha'),
    
    path('cadastro_usuario',views.cadastro_usuario,name='cadastro_usuario'),
    path('index_plataforma',views.plataforma,name='index_plataforma'),
    path('criar_usuario',views.criar_usuario,name='criar_usuario'),
    path('login',views.login,name='login')
]