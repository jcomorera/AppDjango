from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=180)
    imagen = models.ImageField(upload_to=settings.MEDIA_ROOT)
    contenido = models.TextField()
    insertado = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})

class Detalle(models.Model):
    publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=180)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to=settings.MEDIA_ROOT)
    insertado = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.titulo