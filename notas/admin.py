# -*- coding: utf8 -*-
from django.contrib import admin
from models import Cohorte
from models import Periodo
from models import PlanEvaluacion
from models import Notas

# Register your models here.
class CohorteAdmin(admin.ModelAdmin):
    search_fields=['nombre']
admin.site.register(Cohorte, CohorteAdmin)


class PeriodoAdmin(admin.ModelAdmin):
    search_fields=['periodo']
    list_display=('periodo', 'estatus')
admin.site.register(Periodo, PeriodoAdmin)


class PlanAdmin(admin.ModelAdmin):
    search_fields=['actividad']
    list_display=('actividad', 'puntaje', 'cohorte')
admin.site.register(PlanEvaluacion, PlanAdmin)


class NotasAdmin(admin.ModelAdmin):
    list_display=('estudiante', 'actividad', 'nota')
admin.site.register(Notas, NotasAdmin)
