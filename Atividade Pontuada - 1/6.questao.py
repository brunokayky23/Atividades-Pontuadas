import os
os.system("clear")


#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas. 
# O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0), média até 4,0, o aluno está em recuperação, caso a média seja inferior a 4,0 o aluno será reprovado.


nota_um = float(input("Digite a nota 1: "))
nota_dois = float(input("Digite a nota 2: "))

media = (nota_um + nota_dois) // 2
print(media)

if media >= 6:
    print("APROVADO!")
elif media >= 4:
    print("RECUPERAÇÃO!")
elif media < 4:
    print("REPROVADO!")
else: 
    print("APROVADO!")


print('')

print(f"Primeira Nota: {nota_um} ")
print(f"Segunda Nota: {nota_dois} ")


print("==== FIM ====")