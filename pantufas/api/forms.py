from django import forms
from .models import *


class ContatoForm(forms.ModelForm):

    class Meta:

        model = Contato
        # fields = ('nome', 'celular', 'email', 'endereco', 'dia', 'mes', 'ano')
        fields = '__all__'
