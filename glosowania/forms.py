from django import forms
from .models import Decyzja


class DecyzjaForm(forms.ModelForm):

    class Meta:
        model = Decyzja
        fields = ('title', 'tresc', 'kara', 'uzasadnienie', 'znosi')
