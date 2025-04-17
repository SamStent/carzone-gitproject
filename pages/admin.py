from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    # Para poner el thumbnail
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    # Crea los campos que aparecen en la tabla team en el admin.
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    # Hace que se pueda hacer click en el campo.
    list_display_links = ('id', 'thumbnail','first_name',)
    # Crear un campo de búsqueda en el admin.
    search_fields = ('first_name', 'last_name', 'designation')
    # Agregar un filtro.
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
