from django.contrib import admin

# Register your models here.
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'local',)
    list_filter = ('titulo', 'usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)