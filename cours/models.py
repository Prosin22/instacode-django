from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from tinymce.models import HTMLField

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = HTMLField()

    date_pub = models.DateTimeField('date publié')

    class Meta:
        verbose_name_plural = "cours"

    def __str__(self):
        return self.titre

    @property
    def is_pub(self):
        return self.date_pub <= timezone.now()


class Chapitre(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    video_id = models.CharField(max_length=11)
    intro = HTMLField()

    slug = models.SlugField(unique=True, blank=True)
    date_pub = models.DateTimeField('date publié')

    def __str__(self):
        return self.titre

    @property
    def is_pub(self):
        return self.date_pub <= timezone.now()

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(**kwargs)


class Exercice(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    probleme = HTMLField()
    reponse = models.TextField()

    def __str__(self):
        return self.titre
