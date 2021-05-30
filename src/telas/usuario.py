import datetime

from src.failures.usuario_failures import NomeInvalido


def solicita_nome_usuario():
    nome = None
    try:
        nome = input('Digite seu nome ')
        while nome == '':
            print('Nome Inválido')
            nome = input('Digite seu nome ')
    finally:
        return nome


def solicita_data_nascimento_usuario():
    try:
        dia = eval(input('Digite o dia de seu nascimento '))
        mes = eval(input('Digite o mês do seu nascimento '))
        ano = eval(input('Digite o ano do seu nascimento '))
        data_nascimento = datetime.date(ano, mes, dia)
    except ValueError:
        raise DataInvalida
    else:
        return data_nascimento


def converte_data_nascimento_idade(data_nascimento):
    data_atual = datetime.date.today()
    idade = (data_atual - data_nascimento) / 365.25
    return idade.days
