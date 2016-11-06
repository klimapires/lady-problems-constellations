from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    cliente = models.BooleanField()

class JobPost(models.Model):
    title = models.CharField('Título', max_length=128)
    description = models.TextField('Descrição')

    budget = models.DecimalField('Valor', max_digits=6, decimal_places=2)

class JobCategory(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()

class JobArea(models.Model):
    category = models.ForeignKey(JobCategory)
    name = models.CharField(max_length=64)
