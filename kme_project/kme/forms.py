from django import forms

from kme.models import Vlagatelj, Raziskava



class VlagateljForm(forms.ModelForm):

    class Meta:
        model = Vlagatelj
        fields = ('user', 'ime',)#, 'priimek', 'sifra_arrs', 'email')

class RaziskavaForm(forms.ModelForm):
    naslov_raziskave_slo = forms.CharField(label="Naaaaaslov:")

    class Meta:
        model = Raziskava
        fields = ['naslov_raziskave_slo', 'sifra_raziskave', 'tip_raziskave', 'tip_raziskave_drugo']

form_vrstni_red = {"1": VlagateljForm,
                   "2": RaziskavaForm,}
