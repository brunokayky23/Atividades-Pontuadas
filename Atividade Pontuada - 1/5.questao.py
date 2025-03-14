import os 
os.system("clear")

#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
# O programa deve calcular o resultado da operação escolhida aplicado a A e B. 
# Por exemplo, se a operação escolhida foi * e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1*3, que é 3.

valor_a = float(input("Digite um número: "))
operacao = (input("Digite um operador (+ - * /): "))
valor_b = float(input("Digite o segundo número: "))

match operacao:
    case "+":
        resultado = valor_a + valor_b
    case "-": 
        resultado = valor_a - valor_b
    case "*": 
        resultado = valor_a * valor_b
    case "/": 
        resultado = valor_a / valor_b
    case _: 
        resultado = "Opção inválida"


print(f"Primeiro número: {valor_a}")
print(f"Segundo número: {valor_b}")
print(f"Resultado: {resultado}")