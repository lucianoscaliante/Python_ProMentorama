
# importando a biblioteca django DB Models
from django.db import models


class Filmes(models.Model):
    # Definições para as colunas do banco
    nome_do_filme = models.CharField(max_length=50)
    categoria_do_filme = models.CharField(max_length=50)
    Diracao_filme = models.CharField(max_length=50)
    Elenco_filme = models.CharField(max_length=50)
    descricao_filme = models.TextField()

    def __str__(self):
        return self.nome_do_filme
