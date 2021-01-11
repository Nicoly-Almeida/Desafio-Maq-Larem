from django.db import models
from django.contrib.auth.models import AbstractUser


class Contato(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField("nome",max_length = 100)
    celular = models.CharField("celular",max_length = 11)
    email = models.EmailField("email")
    endereco = models.CharField("endereco", max_length = 200)
    dia = models.CharField("dia",max_length = 2)
    mes = models.CharField("mes",max_length = 2)
    ano = models.CharField("ano",max_length = 4)

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    celular = models.CharField("celular",max_length = 11)
    id = models.AutoField(primary_key = True)
    contatos = models.ManyToManyField(Contato, blank = True, null = True)
