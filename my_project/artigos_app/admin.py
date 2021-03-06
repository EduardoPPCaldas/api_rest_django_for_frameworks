from django.contrib import admin
from .models import Autor , Artigo
# Register your models here.

admin.site.register(Autor)

class ArtigoAdmin(admin.ModelAdmin):
  list_display= ('autor', 'titulo' , 'publicado' , 'atualizado')
  class Meta:
    model = Artigo

admin.site.register(Artigo , ArtigoAdmin)