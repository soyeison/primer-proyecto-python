from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Modificado")

    def __str__(self) -> str: # Esto es para que los print que se ven en el administrador sobre la clase post siempre se vean como el titulo
        return self.title
    
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
