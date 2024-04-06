from django.db import models

class Usuarios(models.Model):
    nome = models.TextField(max_length=80)
    email = models.EmailField(max_length=100)
    senha = models.TextField(max_length=16)
