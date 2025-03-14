import os
os.system("clear")


# Faça um algoritmo que leia os valores A, B, C 
# e imprima na tela se a soma de A + B é menor que C, 
# caso contrário, imprima que a A + B é maior que C. 

valor_a = float(input("Digite o primeiro valor: "))
valor_b = float(input("Digite o segundo valor: "))
valor_c = float(input("Digite o terceiro valor: "))

soma = valor_a + valor_b


if soma < valor_c:
    print(f"O valor {soma} é menor que {valor_c}")
elif soma > valor_c: 
    print(f"O valor {soma} é maior que {valor_c}")
else:
    print(f"O valor {soma} é igual a {valor_c}")
print("")