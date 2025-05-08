import os 
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO


# # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#replace ("valor1", "valor2")-> Substitui o valo 1 pelo valor2
#:.2f -> formata para 2 casas decimais apenas no fstring

# n1=float(input("INSIRA A PRIMEIRA NOTA:").replace(",",".")) 
# n2=float(input("INSIRA A SEGUNDA NOTA:").replace(",","."))
# md= (n1+n2)/2
# if md < 5:
#     print("O aluno está reprovado. Média do aluno é", md)
# elif md <= 7:
#      print("O aluno está de recuperação. Média do aluno é", md)
# elif md > 7:
#      print("O aluno está aprovado. Média do aluno é", md)


# peso=float(input("DIGITE O PESO:"). replace (",","."))
# alt=float(input("DIGITE A ALTURA:"). replace (",","."))
# IMC=round( peso/(alt * alt), 2)
# print(f"seu IMC é: {IMC}")
# if IMC < 17:
#     print("Muito abaixo do peso ")
# elif IMC < 18.49 :
#      print("Abaixo do peso")
# elif IMC <= 24.99 :
#      print("peso normal")
# elif IMC <= 29.99 :
#      print("Acima do peso")
# elif IMC <= 34.99 :
#      print("obecidade 1")
# elif IMC <= 39.99 :
#      print("obecidade 2")
# else:
#      print("obecidade 3")




print(r""" 

                       _____________________________________________________  
                      |                                                     | 
             _______  |                                                     | 
            / _____ | |                                                     | 
           / /(__) || |                    __________________]               | 
  ________/ / |OO| || |                                                     | 
 |         |-------|| |                                                     | 
(|         |     -.|| |_______________________                              | 
 |  ____   \       ||_________||____________  |             ____      ____  | 
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |\
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |   
    \__/                   \__/     \__/                    \__/      \__/    




""")
slr= float(input("DIGITE SEU SALÁRIO:"). replace (",",".") )
print("O salário antes do reajuste:",slr)
if slr <= 2799.99:
    print("O percentual do almento aplicado é de: 20%")
    print("O valor do aumento é de:",slr * 0.2)
    n= (slr * 0.2)
    print("O novo salário é de:", slr + n)
elif slr <= 6999.99:
    print("O percentual do almento aplicado é de: 15%")
    print("O valor do aumento é de:",slr * 0.15)
    n= (slr * 0.15)
    print("O novo salário é de:", slr + n)
elif slr <= 14999.99:
    print("O percentual do almento aplicado é de: 10%")
    print("O valor do aumento é de:",slr * 0.1)
    n= (slr * 0.1)
    print("O novo salário é de:", slr + n)
elif slr >= 1500.00:
    print("O percentual do almento aplicado é de: 5%")
    print("O valor do aumento é de:",slr * 0.05)
    n= (slr * 0.05)
    print("O novo salário é de:", slr + n)
