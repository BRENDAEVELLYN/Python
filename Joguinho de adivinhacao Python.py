import random

numero_secreto = random.randint(1,20)

# FIXME:Declarando variáveis

tentativas = 0
max_tentativas = 5
acertou = False

print('Bem - vindo ao Game Python Adivinha!')
print("Você tem {max_tentativas} tentativas para adivinhar o numero secreto entre 1 e 20")

#Loop (Jogo)

while tentativas < max_tentativas:
    palpite = int(input('Digite um numero inteiro:'))

    tentativas += 1

    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um número maior')
    else:
        print('Tente um número menor')
    
    if acertou:
        print(f'Parabéns! Você acertou o numero secreto{numero_secreto} em {tentativas}tentativas')
    else:
        print(f'Que pena! Você não acertou o numero secreto {numero_secreto}')
