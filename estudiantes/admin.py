# -*- coding: utf8 -*-
from django.contrib import admin
from models import Estudiantes
from models import Seccion

# Register your models here.
class EstudiantesAdmin(admin.ModelAdmin):
    search_fields=['cedula']
    list_display=('cedula', 'nombre', 'apellido')
    list_filter=['seccion__nombre']
admin.site.register(Estudiantes, EstudiantesAdmin)


class SeccionAdmin(admin.ModelAdmin):
    search_fields=['asignatura', 'codigo']
    list_display=('nombre', 'asignatura', 'codigo')
admin.site.register(Seccion, SeccionAdmin)
