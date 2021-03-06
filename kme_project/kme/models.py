from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vlagatelj(models.Model):
    user = models.OneToOneField(User)
    ime = models.CharField(max_length=200)
    #priimek = models.CharField(max_length=200)
    #sifra_arrs = models.CharField(max_length=200, blank=True)
    #email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = 'vlagatelji'

    def __str__(self):
        return self.ime

class Raziskava(models.Model):
    TIP_RAZISKAVE_CHOICES = (
        ('DIPL', 'Diplomska naloga'),
        ('KLIN', 'Klinična farmakološka'),
        ('MP', 'Preverjanje medicinskega pripomočka'),
        ('DRUGO', 'Drugo')
    )

    vlagatelj = models.ForeignKey('Vlagatelj')
    naslov_raziskave_slo = models.TextField()
    sifra_raziskave = models.CharField(max_length=200, blank=True)
    tip_raziskave = models.CharField(max_length=200, choices=TIP_RAZISKAVE_CHOICES)
    tip_raziskave_drugo = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'raziskave'

    def __str__(self):
        return self.naslov_raziskave_slo
