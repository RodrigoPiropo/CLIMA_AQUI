from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
