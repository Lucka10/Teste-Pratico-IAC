from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    telefone = models.IntegerField()
    datadenasc = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')


    def __str__(self) -> str:
        return f'{self.nome}\n{self.email}\n{self.telefone}\n{self.datadenasc}\n'


