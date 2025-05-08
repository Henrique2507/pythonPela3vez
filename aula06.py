import os, random
os. system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso ( a partir da versão 3.10)
#match valor:
#   case valor:


# linguagem = 100

# match linguagem:
#     case "python":
#         print(" é facil")
#     case "java":
#         print("muito codigo , python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan nao dorme")
#     case 10:
#         print("entrou aqui !")
#     case _ :
#         print("outro caso")



# print("1-Domingo")
# print("2-Segunda")
# print("3-Terça")
# print("4-Quarta")
# print("5-Quinta")
# print("6-Sexta")
# print("7-Sabado")
# n= int (input("Digite um numero:"))
# match n:
#     case 1:
#         print("Domingo")
#     case 2:
#         print("Segunda")
#     case 3:
#         print("Terça")
#     case 4:
#         print("Quarta")
#     case 5:
#         print("Quinta")   
#     case 6:
#          print("Sexta")  
#     case 7:
#         print("Sabado")

# vlr=0
# vlrf=0
# print("*"*40,"SHOP   DE CELULAR","*"*40)
# print("""
# 1-iphone 15 - R$: 15000
# 2-sansung xl - R$: 10000
# 3-nokia tijolão - R$: 5000
# """)
# cell=int (input("Escolha um dos numeros para escolher o celular:"))
# print("""
# 1-SP- R$: 35
# 2-RJ- R$: 50
# 3-MG- R$: 60
# """)
# etd=int (input("Escolha um dos numeros para escolher o estado:"))
# match cell:
#     case 1:
#         print("valor do celular = R$ 15000") 
#         vlr=15000
#     case 2:
#         print("valor do celular = R$ 1000") 
#         vlr=10000
#     case 3:
#         print("valor do celular = R$ 5000") 
#         vlr=5000
# match etd:
#     case 1:
#         print("valor do frete = R$ 35")
#         vlrf=35
#     case 2:
#         print("valor do frete = R$ 50")
#         vlrf=50
#     case 3:
#         print("valor do frete = R$ 60") 
#         vlrf=60
# print("VALOR TOTAL = ", vlr + vlrf )

# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

print("JOGO PEDRA PAPEL TESOURA")

papel = """
PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador = input("Escolha entre pedra, papel ou tesoura: ")
match jogador:
    case "pedra":
        jogador=pedra
    case "tesoura": 
        jogador =tesoura
    case "papel":
        jogador = papel

#1-> pedra , 2-> papel , 3->tesoura
maquina= random.randint(1,3)
match maquina:
    case 1:
        maquina=pedra
    case 2: 
        maquina =papel
    case 3:
        maquina =tesoura
print(f"voce escolheu  {jogador}")
print(f"maquina escolheu {maquina}")
match jogador:
    case _ if jogador == maquina:
        print("empate")
    case _ if jogador==pedra and maquina ==tesoura:
        print("Voce ganhou")
    case _ if jogador == tesoura and maquina ==papel:
        print("Voce ganhou")
    case _ if jogador == papel and maquina ==pedra:
        print("voce ganhou")
    case _ :
        print("voce perdeu")











































































































































































































































































































































































































































        


