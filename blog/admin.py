from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt', 'updatedAt') # Para mostrar estos elementos pero sin ser editables
    list_display = ('title', 'createdAt', 'updatedAt') # Para ver que columnas puedo ver
    date_hierarchy = 'createdAt'

admin.site.register(Post, PostAdmin) # Esto se usa para extender la configuracion del administrador y registrar el modulo post en el administrador
