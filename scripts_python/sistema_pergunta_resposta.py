# criando a estrutura de dados para perguntas e respostas:

perguntas = [
    {
        'Pergunta': 'quanto é 2+2?',
        'Opções': ['1','2','3','4','5','6','7','8','9'],
        'Resposta':'4',
    },
    {
        'Pergunta': 'quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta':'25',
    },
    {
        'Pergunta': 'quanto é 10/2?',
        'Opções': ['4','5', '2', '1'],
        'Resposta':'5',
    },
]    

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()
    escolha = input("Escolha uma opção:" )

    acertou = False
    escolha_int=None
    qtd_opções= len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opções:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True


    print()

    if acertou:
        qtd_acertos+=1
        print("Acertou 👍")
    else:
        print("Errou ❌")

    
    print()

print("Você Acertou", qtd_acertos)
print("de", len(perguntas), 'perguntas')
    