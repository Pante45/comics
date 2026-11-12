from django.contrib import admin

from .models import Comic, Editorial, Reserva


admin.site.register(Editorial)
admin.site.register(Comic)
admin.site.register(Reserva)