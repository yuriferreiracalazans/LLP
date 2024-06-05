# Definindo a palavra secreta
palavra_secreta = "banana"

# Inicializando variáveis
tentativas_restantes = 3
letras_corretas = []
letras_incorretas = []

# Laço principal do jogo
while True:
    # Mostrando o estado atual da palavra
    palavra_atual = ""
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_atual += letra
        else:
            palavra_atual += "_"
    print("Palavra: ", palavra_atual)
    
    # Verificando se o usuário ganhou
    if "_" not in palavra_atual:
        print("Parabéns, você ganhou!")
        break
    
    # Solicitando uma letra ao usuário
    letra = input("Digite uma letra: ").lower()
    
    # Verificando se a letra já foi tentada
    if letra in letras_corretas or letra in letras_incorretas:
        print("Você já tentou essa letra. Tente novamente.")
        continue
    
    # Verificando se a letra está na palavra secreta
    if letra in palavra_secreta:
        letras_corretas.append(letra)
        print("Letra correta!")
    else:
        letras_incorretas.append(letra)
        tentativas_restantes -= 1
        print("Letra incorreta. Você tem {} tentativas restantes.".format(tentativas_restantes))
    
    # Verificando se o usuário perdeu
    if tentativas_restantes == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)
        break
