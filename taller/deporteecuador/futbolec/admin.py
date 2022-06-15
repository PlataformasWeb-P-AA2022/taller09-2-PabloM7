from django.contrib import admin

# Register your models here.
from futbolec.models import Equipo, Jugador, Campeonato, C_equipos

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre_e','siglas', 'usu_twitter')

admin.site.register(Equipo, EquipoAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_j', 'posicion', 'numero', 'sueldo','equipo')

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_c', 'auspiciante')

admin.site.register(Campeonato, CampeonatoAdmin)

class C_equiposAdmin(admin.ModelAdmin):
    list_display = ('año', 'equipo', 'campeonato')

admin.site.register(C_equipos, C_equiposAdmin)