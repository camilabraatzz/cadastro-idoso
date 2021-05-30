def classificacao_OMS(pessoa):
    mensagem_padrao = 'Classificação de acordo com a OMS: \n'
    mensagem_meia_idade = mensagem_padrao + 'Meia-Idade(45 a 59 anos)'
    mensagem_idoso = mensagem_padrao + 'Idoso(60 a 74 anos)'
    mensagem_anciao = mensagem_padrao + 'Ancião(75 a 90 anos)'
    mensagem_velhice_extrema = mensagem_padrao + 'Velhice extrema(90 anos em diante)'
    mensagem_jovem = mensagem_padrao + 'Não se enquadra na classificação de envelhecimento'
    if 45 <= pessoa['idade'] < 59:
        mensagem = mensagem_meia_idade
    elif 60 <= pessoa['idade'] < 74:
        mensagem = mensagem_idoso
    elif 75 <= pessoa['idade'] < 90:
        mensagem = mensagem_anciao
    elif pessoa['idade'] > 90:
        mensagem = mensagem_velhice_extrema
    else:
        mensagem = mensagem_jovem

    return mensagem
