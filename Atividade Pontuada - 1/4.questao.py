import os
os.system("clear")

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

print("""
Tabela das Frutas                
 Frutas \t Até 5kg \t\t Acima de 5kg 
Morango \t R$ 2,50 POR Kg\t\t  R$ 2,20 por Kg 
Maçã \t\t R$ 1,80 por Kg \t R$ 1,50 por Kg      
""")

# Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas 
# e escreva o valor a ser pago pelo cliente.


morango = int(input("Digite quantos quilos de morangos foram comprados: "))
macas = int(input("Digite quantos quilos de maçãs foram comprados: "))



if morango <= 5:
    valor_morango = morango * 2.5
else: 
    valor_morango = morango * 2.2

if macas <= 5:
    valor_macas = macas * 1.8
else:
    valor_macas = macas * 1.5


valor = valor_morango + valor_macas

if (morango + macas) >= 10 or valor > 15:
    desconto = valor * 0.1
    valor_final = valor - desconto
    print(f"Valor do Morango: {valor_morango:.2f}")
    print(f"Valor das maçãs: {valor_macas:.2f}")
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
else:
    print(f"Valor do Morango: {valor_morango}")
    print(f"Valor das maçãs: {valor_macas}")
    print(f"Valor a ser pago R$ {valor:.2f}")


  
    