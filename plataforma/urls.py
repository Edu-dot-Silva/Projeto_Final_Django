from django.urls import path
from . import views

urlpatterns = [
    path('index_plataforma',views.plataforma,name='plataforma'),
    
]