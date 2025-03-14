import os
os.system("clear")


# Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

# Álcool - Até 25 l, desconto de 2%
# Álcool - Acima de 25 l, desconto de 4%
# Gasolina - Acima de 25 l, desconto de 5%
# Gasolina - Até 25 l, desconto de 3%

#Escreva um algoritmo que 
# leia o número de litros vendidos e o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.


tipo_combustivel = input("""                
A - Álcool,                          
G - Gasolina
Digite o tipo de combustível:                     
""").upper()
litros_vendidos = float(input("Digite o número de litros vendidos: "))
preco_alcool = 3.79
preco_gasolina = 6.59

match tipo_combustivel:
    case "A": 
        preco_total = litros_vendidos * preco_alcool
        
        if litros_vendidos <= 25:
            desconto = preco_total * 0.02 
        else: 
            desconto = preco_total * 0.04  

    case "G":  
        preco_total = litros_vendidos * preco_gasolina
        if litros_vendidos <= 25:
            desconto = preco_total * 0.03  
        else:
            desconto = preco_total * 0.05  

    case _: 
        print("Tipo de combustível inválido")
        desconto = 0
        preco_total = 0


valor_a_pagar = preco_total - desconto

print("")

print(f"Litros vendidos: {litros_vendidos}")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

