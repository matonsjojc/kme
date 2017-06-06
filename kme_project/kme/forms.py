from django import forms

from kme.models import Vlagatelj, Raziskava

class VlagateljForm(forms.ModelForm):
    ime = forms.CharField(max_length=200,
                          help_text="Ime")
    priimek = forms.CharField(max_length=200,
                              help_text="Priimek")
    sifra_arrs = forms.CharField(max_length=200,
                                 help_text="ce obstaja")
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Vlagatelj
        fields = ('ime', 'priimek', 'sifra_arrs', 'email')
