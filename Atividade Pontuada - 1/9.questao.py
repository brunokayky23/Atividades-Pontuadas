import os
os.system("clear")


#Uma financeira usa o seguinte critério para conceder empréstimos: 
# o valor total do empréstimo deve ser até dez vezes o valor da renda mensal do solicitante 
# e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante. 
# Escreva um programa que leia a renda mensal de um solicitante, 
# o valor total do empréstimo solicitado e o número de prestações que o solicitante deseja pagar 
# e informe se o empréstimo pode ou não ser concedido.



renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do empréstimo: "))
numero_prestacoes = int(input("Digite o número de prestações: "))

valor_prestacao = valor_emprestimo / numero_prestacoes

emprestimo_max = renda_mensal * 10
prestacao_max = renda_mensal * 0.3

if valor_emprestimo <= emprestimo_max and valor_prestacao <= prestacao_max:
    print("Empréstimo APROVADO!")
    print(f"Valor de cada prestação: R$ {valor_prestacao:.2f}")
else:
    print("Empréstimo NEGADO!")
