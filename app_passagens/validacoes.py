from datetime import date
def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais!'


def verificar_digito(valor_campo, nome_campo, lista_de_erros):

    """verifica se possui algum digito numerico"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Campo não pode conter números'

def validacoes_data(data_ida, data_volta, data_pesquisa, lista_de_erros):
    """Verifica se data de ida eh maior que data volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de ida não pode ser maior que data de volta!'

    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data invalida.'


