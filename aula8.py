# ATV.1 
# ESCREVA UM PROGRAMA QUE PEÇA AO USUÁRIO PARA INSERIR DOIS NÚMEROS 
# E VERIFIQUE SE O PRIMERO NÚMERO É DIVISÍVEL PELO SEGUNDO USANDO O OPERADOR DE MÓDULO.
n1 = int(input("Escolha um número:"))
n2 = int(input("Escolha um número:"))

if n1 % n2 == 0:
    print(n1,'é divisível por',n2)
else:
    print(n1,'não é divisível por',n2)

# ATV.2
# ESCREVA UM PROGRAMA QUE VERIFIQUE SE UM DETERMINADO ANO É BISSEXTO 
# OU NÃO USANDO O OPERADOR DE MÓDULO.  
def bissexto(ano):
    if (ano % 4 == 0):
        return True
    else:
        return False

ano = int(input("Digite um ano: "))

if bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

# ATV.3
# ESCREVA UM PROGRAMA PARA MULTIPLICAR POR 3 ,
# OS NÚMEROS PARES DE UMA LISTA.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiplica_pares_por_3(lista):
    resultado = []
    for numero in lista:
        if numero % 2 == 0:  # Verificando se o número é par
            resultado.append(numero * 3)
    return resultado

# Chamada da função para multiplicar os números pares por 3
resultado = multiplica_pares_por_3(lista)
print("Lista original:", lista)
print("Números pares multiplicados por 3:", resultado)

