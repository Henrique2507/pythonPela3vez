import os
os.system("cls")

#Continuação Input com Int e Float
#int ()-> converte para inteiro
#float()-> converte para numero quebrado

#exemplo 1
# numero= 10
# numero2= input("digite um numero")
# print("o tipo de numero é,", type(numero2))
# soma= numero + int(numero2)
# print(f"soma de {numero} + {numero2} = ", soma)

#exemplo 2
# numero1= input("digite uum numero: ")
# soma= float (numero1) + 15
# print("A soma de ",numero1 , "+", "15", "=", soma)

#exemplo 3
# n1=float(input("digite um numero: "))
# n2= float(input("digite outro numero: "))

# soma= n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)


#atividade1-
# num1=int(input("digite um numero: "))
# num2=int(input("digite outro numero: "))
# multiplicacao = num1 * num2
# print(f"a multiplicacao de {num1} * {num2} =", multiplicacao )


# #atividade2-
# num1=int(input("digite um nuumero: "))
# sucessor= num1 + 1
# antecessor= num1 - 1
# print("antecessor =", sucessor )
# print("sucessor =", antecessor )

# #atividae3-
# ano1=2025
# ano2= int(input("digite o ano: "))
# print(f" {ano2} - {ano1} =", ano1 - ano2 )

#PORCENTAGEM
# print("25% de 100 = ", 0.25 * 100)
# print("4% de 400 = ", 0.04 * 400)
# print("99% de 1525 = ", 0.99 * 1525)

#supondo que um produto custa 150 reais
#e o caixa deu um desconto de 15%
# exemplo= float(input("digite o preco do produto"))
# desconto= 0.15 * exemplo
# print("o preco do produto com 15 % de dessconto é ", exemplo)


print("", "MERCADO","", sep="="*30)
itm1= (input("primeiro item: "))
vlr1= float(input("valor do primeiro item: "))
itm2= (input("segundo item: "))
vlr2= float(input("valor do segundo item: "))
dct1= 0.1 * vlr1
dct2= 0.25 * vlr2
custo1=vlr1-dct1
custo2=vlr2-dct2
print("", "CAIXA","", sep="="*30)
print(itm1, "custa", vlr1, "com 10% de desconto =", "R$ ", custo1)
print(itm2, "custa", vlr2, "com 25% de desconto =", "R$ ", custo2)
ttl=custo1 + custo2
print("", "","" ,sep="-"*30)
print("TOTAL R$: ", ttl)

#round(valor,qtdCasasDecimais) -> faz o arredondamento dos valores 