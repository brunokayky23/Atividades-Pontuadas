import os
os.system("clear")


# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, 
# caso contrário multiplique A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

valor_a = float(input("Digite o primeiro valor: "))
valor_b = float(input("Digite o segundo valor: "))

if valor_a == valor_b:
    soma = valor_a + valor_b  
    valor_c = soma
else:
    multiplica = valor_a * valor_b
    valor_c = multiplica




print(f"Resultado: {valor_c}")
