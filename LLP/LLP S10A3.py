# Laço externo para iterar sobre as tabuadas de 1 a 5
tabuada = 1
while tabuada <= 5:
    print(f"Tabuada do {tabuada}:")
    # Laço interno para iterar sobre os números de 1 a 10 de cada tabuada
    numero = 1
    while numero <= 10:
        produto = tabuada * numero
        print(f"{tabuada} x {numero} = {produto}")
        numero += 1
    # Próxima tabuada
    tabuada += 1
    print()
