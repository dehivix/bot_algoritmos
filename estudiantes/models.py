# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    cedula = models.CharField(max_length=50,unique=True,verbose_name=u'Número de Identificación')
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    seccion = models.ForeignKey('Seccion')
    class Meta:
        db_table = u'estudiantes'
        verbose_name_plural = "estudiantes"
    def __unicode__(self):
        return u'%s %s %s'%(self.cedula, self.apellido, self.nombre)


class Seccion(models.Model):
    nombre = models.CharField(max_length=100,)
    asignatura = models.CharField(max_length=100,)
    codigo=models.CharField(max_length=10,blank=True,null=True)
    class Meta:
        db_table = u'secciones'
        verbose_name_plural = 'secciones'
    def __unicode__(self):
        return u'%s'%(self.nombre)
