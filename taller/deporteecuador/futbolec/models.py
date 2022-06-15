from pyexpat import model
from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre_e = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    usu_twitter = models.CharField(max_length=30)

    def __str__(self):
        return "%s | %s | %s" % (self.nombre_e, 
                self.siglas,
                self.usu_twitter)

class Jugador(models.Model):
    nombre_j = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero = models.IntegerField("numero de jugador")
    sueldo = models.IntegerField("sueldo de jugador")
    equipo = models.ForeignKey(Equipo, related_name='jugadores',on_delete=models.CASCADE)

    def __str__(self):
        return "%s | %s | numero: %d | sueldo: %d - %s" % (self.nombre_j, 
                self.posicion,
                self.numero,
                self.sueldo, 
                self.equipo.nombre_e)

class Campeonato(models.Model):
    nombre_c = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    def __str__(self):
        return "%s | %s" % (self.nombre_c,
                self.auspiciante)

class C_equipos(models.Model):
    año = models.IntegerField("Año")
    equipo = models.ForeignKey(Equipo, related_name='equipos',on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='campeonato', on_delete=models.CASCADE)

    def __str__(self):
        return "año: %d | %s | %s" % (self.año, 
                self.equipo.nombre_e,
                self.campeonato.nombre_c)