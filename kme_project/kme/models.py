from django.db import models

# Create your models here.
class Vlagatelj(models.Model):
    ime = CharField(max_length=200)
    priimek = CharField(max_length=200)
    sifra_arrs = CharField(max_length=200, blank=True)
    email = EmailField(max_length=254)

class Raziskava(models.Model):
    TIP_RAZISKAVE_CHOICES = (
        ('DIPL', 'Diplomska naloga'),
        ('KLIN', 'Klinična farmakološka'),
        ('MP', 'Preverjanje medicinskega pripomočka'),
        ('DRUGO', 'Drugo'),

    naslov_raziskave_slo = TextField()
    sifra_raziskave = CharField(max_length=200)
    tip_raziskave = CharField(max_length=200, choices=TIP_RAZISKAVE_CHOICES)
    tip_raziskave_drugo = CharField(max_length=200, blank=True)
