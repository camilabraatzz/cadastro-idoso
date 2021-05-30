from src.pessoa import Pessoa
from src.telas.usuario import converte_data_nascimento_idade, solicita_nome_usuario, solicita_data_nascimento_usuario
from src.utils.mensagens import classificacao_OMS


def UsuarioInteracoes():
    pessoa_maior_idade = None
    maior_idade = 0
    pessoas = []
    count = 1
    while True:
        print(f'Pessoa {count}')
        pessoa = Pessoa()
        pessoa.nome = solicita_nome_usuario()
        if pessoa.nome == 'Fim' or pessoa.nome == 'fim':
            break
        pessoa.data_nascimento = solicita_data_nascimento_usuario()
        dic_pessoa = {
            'nome': pessoa.nome,
            'idade': converte_data_nascimento_idade(pessoa.data_nascimento)
        }
        pessoas.append(dic_pessoa)
        if dic_pessoa['idade'] > maior_idade:
            pessoa_maior_idade = dic_pessoa
            maior_idade = dic_pessoa['idade']
        count += 1
        print(classificacao_OMS(dic_pessoa))
        print('='*35)
    print(f'Pessoas cadastradas: {pessoas}')
    print(f'Pessoa mais velha: {pessoa_maior_idade}')


UsuarioInteracoes()
