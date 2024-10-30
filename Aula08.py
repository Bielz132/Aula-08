# SISTEMA DE BANCO
nome = 'gabriel'
senha = 123
gmail = 'gabriel@gmail.com'

print('Ola, seja bem vindo ao banco "Boca Da Fortuna"')
for n in range(1,3):
    nome_user = input('Digite seu nome: ')
    senha_user = int(input('Digite sua senha: '))
    gmail_user = input('Digite seu gmail: ')
    if nome_user == nome and senha_user == senha and gmail_user == gmail:
        print(f'Seja bem vindo {nome}')
        print(f''' Você gostaria de fazer oque?
        Ver extrato = 1
        Fazer deposito = 2
        fazer saque = 3
        sair do sistema = 4''')
        escolha = input('-> ')
        
        break

    
    else:
        print('Tente novamente')    