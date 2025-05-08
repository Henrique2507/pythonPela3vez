import os
os.system("cls")

# #aula02 -> variaveis, tipos e input
#Tipos de dados
#string -> Texto
#Int -> Inteiro
#Float -> quebrado (flutuante)

# declaração de variaveis 
# escola = "senai"

# #mostrando o valor da variavel no print
# #concatenando com o +
# print("o nome da minha escola é " + escola)
# #separando por parametro ,
# print("o nome da minha escola é", escola)
# #f string {} -> mostra o valor da variavel dentro das aspas
# print(f"o nome da minha escola é {escola}")

# #exemplo de variavel int
# numero =100
# print("somando com 10 = ",numero +10)
# print("subtraindo 5 =",numero -5)
# print("dividindo por 2",numero /2)
# print("multiplicando por 10 =",numero *10)

#atividade 1-
# nome= "Henrique"
# idade= "16"
# cpf= "453.905.398-18"
# print("meu nome é", nome)
# print("tenho", idade, "anos")
# print("e meu cpf é", cpf)

#input
#Obrigadoriamente antes do input deve existir uma variavel
# resumindo...
#input() -> pergunta algo a ser armazenado
#print() -> mostra o texto na tela
# texto= input("digiti algo:")
# print("voce digitou ...", texto)


#atividade 2-
print("","CADASTRO","",sep="*"*15 )
print("\n")
nome=""
cpf=""
rg=""
nome= input("digite seu nome:")
cpf= input("digite seu cpf:")
rg= input("digite seu rg:")
print("","CADASTRO","",sep="*"*5 )
print("Nome:",nome)
print("Cpf:",cpf)
print("Rg:",rg)