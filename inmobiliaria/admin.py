from django.contrib import admin

from . import models


class PropiedadInline(admin.TabularInline):
    model = models.inmobiliaria
    extra = 1


@admin.register(models.Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "region", "codigo_clasificacion", "activa")
    list_filter = ("activa", "region")
    search_fields = ("nombre", "region", "codigo_clasificacion")
    inlines = (PropiedadInline,)


@admin.register(models.inmobiliaria)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_propiedad",
        "direccion",
        "tipo_propiedad",
        "precio_arriendo",
        "disponible",
        "comuna",
        "inmobiliaria_comuna",
    )
    list_filter = ("tipo_propiedad", "disponible", "comuna")
    search_fields = (
        "codigo_propiedad",
        "direccion",
        "comuna__nombre",
        "inmobiliaria_comuna__username",
    )
    actions = ("marcar_disponibles", "marcar_arrendado")

    @admin.action(description="Marcar propiedades como disponibles")
    def marcar_disponibles(self, request, queryset):
        queryset.update(disponible=True)

    @admin.action(description="Marcar propiedades como no disponibles")
    def marcar_arrendado(self, request, queryset):
        queryset.update(disponible=False)
