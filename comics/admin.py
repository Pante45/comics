from django.contrib import admin

from .models import Comic, Editorial, Reserva


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'editorial',
        'numero_tomo',
        'stock',
        'precio_en_pesos',
        'tapa_dura',
        'disponible',
    )
    list_filter = ('editorial', 'tapa_dura')
    search_fields = ('titulo',)

    @admin.display(description='Precio')
    def precio_en_pesos(self, comic):
        return f'${comic.precio:,.0f}'.replace(',', '.')


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'comic',
        'nombre',
        'rut',
        'cantidad',
        'fecha_reserva',
    )
    list_filter = ('comic',)
    search_fields = ('nombre', 'rut')