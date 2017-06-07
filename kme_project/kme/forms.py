from django import forms

from kme.models import Vlagatelj, Raziskava



class VlagateljForm(forms.ModelForm):
    """ime = forms.CharField(max_length=200,
                          label="Ime")
    priimek = forms.CharField(max_length=200,
                              label="Priimek")
    sifra_arrs = forms.CharField(max_length=200,
                                 label="ARRS šifra:",
                                 required=False)
    email = forms.EmailField(max_length=254,
                             label="email:")
"""
    class Meta:
        model = Vlagatelj
        fields = ('ime',)#, 'priimek', 'sifra_arrs', 'email')

class RaziskavaForm(forms.ModelForm):
    naslov_raziskave_slo = forms.CharField(label="Naaaaaslov:")

    class Meta:
        model = Raziskava
        fields = ['naslov_raziskave_slo', 'tip_raziskave']

form_vrstni_red = {"1": VlagateljForm,
                   "2": RaziskavaForm,}
