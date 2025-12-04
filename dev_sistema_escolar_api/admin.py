

from django.contrib import admin
from dev_sistema_escolar_api.models import *


@admin.register(Administradores)
class AdministradoresAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")


@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")


@admin.register(Maestros)
class MaestrosAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "update")
    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

