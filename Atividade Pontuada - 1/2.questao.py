import os
os.system("clear")


# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).
# Por fim, mostre os dados do usuário.


nome = input("Digite seu nome: ")

sexo = input("""
M - Masculino
F - Feminino             
Digite a letra correspondente ao seu sexo:
""").upper() 


estado_civil = input("""
Casado(a)
Solteiro (a)
Digite seu estado civil: 
""").upper()



if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Quantos anos você está casada? "))
    print("")
    print(f"Tempo de casada: {tempo_casada} anos")
else:
    print("")


print(f"Nome: {nome}")
match sexo:
    case "f" |"F":
        print("Sexo: Feminino")
    case "m"| "M":
        print("Sexo: Masculino")
    case _: 
        print("O sexo não consta, digite novamente!" )
print(f"Estado Civil: {estado_civil}")