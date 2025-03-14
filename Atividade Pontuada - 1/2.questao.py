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
while sexo not in ["M", "F"]:
    print("Resposta errada! Digite 'M' para masculino ou 'F' para feminino.")
    sexo = input("Digite seu sexo corretamente (M para Masculino, F para Feminino): ").upper()

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

if sexo == "F":
    print("Sexo: Feminino")
else:
    print("Sexo: Masculino")

print(f"Estado Civil: {estado_civil}")