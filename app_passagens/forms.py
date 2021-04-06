from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import date
from app_passagens.classe_viagem import tipos_de_classes
from app_passagens.validacoes import *
from app_passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=date.today())

    class Meta:
        model = Passagem
        fields = '__all__' # traz todos os campos do formulario
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data de volta', 'informacoes': 'Informações'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }



    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}

        verificar_digito(origem, 'origem', lista_de_erros)
        verificar_digito(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        validacoes_data(data_ida, data_volta, data_pesquisa, lista_de_erros)


        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_de_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_de_erro)

        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa# informa o nome do modelo
        exclude =['nome']