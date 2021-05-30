class NomeInvalido(Exception):
    def __init__(self, mensagem='Digite um nome válido!'):
        self.mensagem = mensagem


class DataInvalida(Exception):
    def __init__(self, mensagem='Digite uma data válida!'):
        self.mensagem = mensagem