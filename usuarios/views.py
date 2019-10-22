from django.shortcuts import render
from django.views.generic.base import View


from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm

from django.contrib.auth.models import User

from django.shortcuts import redirect
#

class RegistrarUsuarioView(View):
    
    template_name = 'registrar.html'

    def get(self,request):

        return render(request, self.template_name) 

    def post(self, request):

        # Preencher o form 
        form = RegistrarUsuarioForm(request.POST) # Método POST é usado para requisição de dados incorporado dentro da mensagem !

        #Verificar se eh valido 

        if form.is_valid():

            dados_form = form.data

            #Criar usuario

            usuario = User.objects.create_user(dados_form['nome'],dados_form['email'],dados_form['senha'])

            #Criar Perfil
            perfil = Perfil(nome=dados_form['nome'],telefone=dados_form['telefone'],nome_empresa=dados_form['nome_empresa'],usuario=usuario)


            #Gravar No Banco

            perfil.save()

            #Redirecionando para o Index

            return redirect('index')

            #so chega aqui se nao for valido
            #vamos devolver o form para mostrar o formulario preenchido 

            return render(request, self.template_name,{'form' : form})



       # return render(request, self.template_name)