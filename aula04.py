import os
os.system("cls")

#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)


#ATIVIDADE 1 E 2
# ida=float(input("Quantos anos voce tem: "))
# if ida < 0 or ida > 120:
#     print("ERROR")
# else:
#     if ida >= 18:
#         print("VOCE É MAIOR DE IDADE ")
#     else:
#         print("VOCE É MENOR DE IDADE")

#ATIVIDADE 3
# mail= input("digite o e-mail do usuario: ")
# sn= input("digite sua senha: ")
# if mail == "python@senai.com" and sn == "12345678":
#     print("USUARIO AUTENTICADO")
# else:
#     print("USUARIO ou senha Inválidos")

#ATIVIDADE 4
# print("*"*25,"LOJA DE MAÇÃS","*"*25)
# mç=float(input("QUANTAS MAÇÃS GOSTARIA DE LEVAR:"))
# if mç >= 12:
#     preço= 0.25
# else:
#     preço= 0.30
# print("maças, total:R$", mç * preço)


#upper() -> CONVERTER TUDO PARA MAIUSCULO
#lower() -> CONVERTER TUDO PARA MINUCULO

#ATIVIDADE 1
# vc= input("DIGITE UMA LETRA:").lower()
# if vc =="a"  or vc =="e"  or vc =="i" or vc =="o" or vc =="u":
#     print("vogal")
# else:
#     print("consoante")

#reescrevendo de outra maneira
# and  or  in 
# l = input("Digite uma letra")
# if l in "aeiouAEIOU"
#     print("vogal")
# else:
#     print("consoante")

#ATIVIDADE 2
n1=float(input("DIGITE O PRIMEIRO NUMERO:"))
n2=float(input("DIGITE OUTRO NUMERO:"))
if n1 > n2:
     print("Maior:", n1)
else: 
     print("Menor", n2)