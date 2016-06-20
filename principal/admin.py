from django.contrib import admin

from .models import Categoria, Noticias, Comentario

class NoticiaAdmin(admin.ModelAdmin):
    list_display=('id', 'titulo', 'creado_por', 'creado_el')
    list_display_links = ('titulo',)
    search_fields = ['titulo', 'creado_el']
    list_filter = ('creado_por', 'creado_el', )



admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Noticias, NoticiaAdmin)

