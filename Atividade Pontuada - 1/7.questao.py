import os
os.system("clear")

# Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. 
# Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar 
# (total a pagar = total - desconto), sabendo-se que: 
# Se quantidade <= 5 o desconto será de 2% 
# Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
# Se quantidade > 10 o desconto será de 5%.

nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida do produto: "))
preco_unitario = float(input("Digite o preço do produto: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02
if quantidade <= 10:
    desconto = total * 0.03
if quantidade > 10:
    desconto = total * 0.05

total_a_pagar = total - desconto

print("")
print("")

print(f"Nome do Produto: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço Unitário: {preco_unitario}")
print(f"Preço do produto: {total}")
print(f"Desconto: {desconto}")
print(f"Total a Pagar: {total_a_pagar}")