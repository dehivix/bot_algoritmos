# -*- coding: utf8 -*-
from django.db import models
from estudiantes.models import Estudiantes
from estudiantes.models import Seccion

# Create your models here.
class Cohorte(models.Model):
    nombre = models.CharField(choices=(('Primer','Primer'),('Segundo','Segundo'), ('Tercer', 'Tercer')),default=0,max_length=8, verbose_name=u'Seleccione cohorte')
    periodo = models.ForeignKey('Periodo')
    seccion = models.ForeignKey(Seccion)
    class Meta:
        db_table = u'cohorte'
        verbose_name_plural = 'cohortes'
    def __unicode__(self):
        return u'%s'%(self.nombre)


class Periodo (models.Model):
    periodo = models.CharField(max_length=10,verbose_name='período')
    estatus = models.BooleanField()
    class Meta:
        db_table = u'periodos'
        verbose_name_plural = 'periodos'
    def __unicode__(self):
        return u'%s'%(self.periodo)


class PlanEvaluacion(models.Model):
    actividad = models.CharField(max_length=100,)
    puntaje = models.CharField(max_length=10,blank=True,null=True)
    cohorte = models.ForeignKey('Cohorte')
    class Meta:
        db_table = u'plan'
        verbose_name_plural = 'planes'
    def __unicode__(self):
        return u'%s'%(self.actividad)


class Notas(models.Model):
    estudiante = models.ForeignKey(Estudiantes)
    actividad = models.ForeignKey('PlanEvaluacion')
    nota = models.CharField(max_length=100,)
    class Meta:
        db_table = u'notas'
        verbose_name_plural = 'notas'
    def __unicode__(self):
        return u'%s %s %s'%(self.estudiante, self.actividad, self.nota)
