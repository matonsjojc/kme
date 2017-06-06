from django.contrib import admin

# Register your models here.
from kme.models import Vlagatelj, Raziskava

class VlagateljAdmin(admin.ModelAdmin):
    fields = ['ime', 'priimek', 'sifra_arrs', 'email']

class RaziskavaAdmin(admin.ModelAdmin):
    list_display = ('naslov_raziskave_slo', 'sifra_raziskave', 'tip_raziskave', 'tip_raziskave_drugo')

admin.site.register(Vlagatelj, VlagateljAdmin)
admin.site.register(Raziskava, RaziskavaAdmin)
