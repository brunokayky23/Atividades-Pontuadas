import os
os.system("clear")


# Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. 
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço. 
# A loja está atualmente com a seguinte tabela de preços. 


print("""
Tabela das cores dos CD's              
  \t CD'S \t\t Preço
 \t Verde \t\t  R$ 10,00
 \t Azul \t\t R$ 20,00  
 \t Amarelo \t R$ 30,00  
 \t Vermelho \t R$ 40,00  
""")

cor = input("Digite a cor do CD: ").upper().lower()


match cor:
    case "verde":
        preco = 10
    case "azul":
        preco = 20
    case "amarelo":
        preco = 30
    case "vermelho":
        preco = 40



print(f"O cd de cor {cor} custa {preco:.2f}")