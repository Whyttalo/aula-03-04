'''import random
print("$$$ Inicio do jogo $$$")

def gera():
    return random.randint(1,100)

def jogo():
    resposta = gera()
    tentativa = 0
    
    print("Palpite gerado!")
    print("VAMOS COMEÇAR?")

    chute = 0

    while chute is not resposta:
        tentativa +=1
        chute = int(input("QUAL SEU CHUTE DE 0 A 100"))
        if tentativa >= 10:
            print("PERDEUUU ESGOTARAM SUAS TENTATIVAS!!!")
            print("$$$COLOCAR MAIS FICHAS$$$")
            break
        if chute > resposta:
            print("ERROU! É UM NÚMERO MENOR", chute)
        
        elif chute < resposta:
            print("ERROU! É UM NÚMERO MAIOR", chute)
        else:
            print("PARABÉNS ACERTOUUUU!!!! O NÚMERO GERADO FOI", resposta)
            print("O NÚMERO DE TENTATIVAS FOI", tentativa)
            break

jogo()'''


'''import random

def jogo_advinha():
    numero_aleatorio = random.randint(1,100)
    tentativas = 0
    print("Bem vindo ao jogo")
    while True:
        palpite = int(input(" tente adivinhar o número (entre 1 e 100)"))
        tentativas +=1

        if palpite < numero_aleatorio:
            print("Tá baixo! tente novamente")
        elif palpite > numero_aleatorio:
            print("Tá alto! ")
        else:
            print(f"Parabéns, você acertou o número {numero_aleatorio} em {tentativas} tentativas!")
            break

jogo_advinha()'''

#Medição de area!:
import math

def area(raio):
  return math.pi*raio**2

def perimetro(raio):
  return 2 *math.pi*raio

def menu():
  raio = float(input("insira o raio."))

  while True:
    print("1. Calcular área: ")
    print("2. Calcular perimetro: ")
    print("3. Sair")
    
    opcao = input("Escolaha uma opção.")
    print("Você escolhe a opção: ",opcao)
    if opcao == '1' :
      a = area(raio)
      print(f'A area de circulo é: {a: .2f}')
    elif opcao == '2' :
      p = perimetro(raio)
      print(f' O perimetro do circulo é: {p: .2f}')
    elif opcao == '3' :
      print("Saindo...")
    break

    menu()
menu()
