from django.contrib import admin
from django.views.generic import list

from .models import Publicacion
from .models import Detalle

# Register your models here.
class PublicacionModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","insertado","actualizado"]
    #list_display_links = ["actualizado"]
    list_filter = ["insertado","actualizado"]
    search_fields = ["titulo","contenido"]
    class Meta:
        model = Publicacion

admin.site.register(Publicacion,PublicacionModelAdmin)

class DetalleModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","insertado","actualizado"]
    list_filter = ["insertado","actualizado"]
    search_fields = ["titulo","publicacion"]
    class Meta:
        model = Detalle

admin.site.register(Detalle,DetalleModelAdmin)