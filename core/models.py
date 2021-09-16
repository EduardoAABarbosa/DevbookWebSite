from django.db import models

class Depoimentos(models.Model):
    nome=models.CharField('Nome',max_length=100)
    cargo=models.CharField('Cargo',max_length=100)
    foto=models.ImageField('Foto',upload_to='foto')
    depoimento=models.CharField('Depoimento',max_length=200)