from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=350)
    slug = models.SlugField()


# Pour la table BlogPost
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Clé etrangaire 1 a Plusieur
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)  # longeur du text est de 100 caracteur
    slug = models.SlugField()  # permet d'afficher le titre de l'article en url.
    published = models.BooleanField(default=False)  # default permet d'afficher par defaut un champ
    date = models.DateField(blank=True, null=True)  # prend la valeur null par defaut
    content = models.TextField()
    description = models.TextField()
