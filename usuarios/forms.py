from django import forms
from django.contrib.auth.models import User # Importe para usuario já existem ou já registrado
class RegistrarUsuarioForm(forms.Form):

    nome  = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)   
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid=False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existe')
            valid = False

        return valid


    def adiciona_erro(self,menssage):
        errors = self._errors.setdefaut(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorLis())
        errors.append(menssage)

