# Crie um sistema de e-commerce, onde o usuário possa cadastrar-se, comprar um produto, descobrir o valor total e pagar

for n in range(11):
    print(n)
    
for variavel in range(0,11,2):
    print(variavel)
    
lista = [1,2,3]
for c in lista:
    print(c)
#---------------------------------------------
lista = []
for n in range(1,3):
    print('Cadastre-se')
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    email = input('Digite seu e=mail: ')
    print('Obrigado, proximo cliente')
    lista += (nome, idade, email)
print(lista)

numero = int(input('-> '))          
for n in range(0,11):
    result = n * numero
    print(f'{n} X {numero} = {result}')
#---------------------------------------------
chances = list(range(1,4))

for n in chances:
    chute = int(input('Digite um número: '))
    aleatorio = random.randint(1,6)
    if chute == aleatorio:
        print('Parabéns, acertou em cheio!')
        break
    else:
        print('Que pena, o numero é', aleatorio)
        
    
    
    