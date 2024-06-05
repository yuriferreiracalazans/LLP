# Pedir ao usuário para inserir um número
numero = int(input("Insira um número: "))

# Usar um laço for para percorrer um intervalo de 1 a 10
for i in range(1, 11):
    # Calcular o produto do número fornecido pelo valor atual do laço
    produto = numero * i
    # Imprimir cada produto em uma nova linha
    print(numero, "x", i, "=", produto)
