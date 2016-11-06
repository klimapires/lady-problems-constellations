from django.db import models

class JobPost(models.Model):
    title = models.CharField('Título', max_length=128)
    description = models.TextField('Descrição')

    budget = models.DecimalField('Valor', max_digits=6, decimal_places=2)
