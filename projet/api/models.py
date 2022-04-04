from django.db import models

class Table(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=100)

# Create your models here.
