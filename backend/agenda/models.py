from django.db import models

def diretorio_imagens(instance, filename):
    return 'agenda/fotos/{0}{1}'.format(instance.id, filename)

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(default='email@default')
    telefone = models.CharField(max_length=11)
    datadenasc = models.DateField(default='1900-01-01',verbose_name='Data de nascimento')
    foto = models.ImageField(default=f'agenda/fotos/profilebase.jpeg',upload_to=diretorio_imagens)


    def __str__(self) -> str:
        return f'{self.nome}\n{self.email}\n{self.telefone}\n{self.datadenasc}\n'


