import random

def jogo_adivinhacao():
    # Gerar um número aleatório entre 1 e 50
    numero_secreto = random.randint(1, 50)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação! Você tem 5 tentativas para adivinhar o número secreto entre 1 e 50.")
    
    while tentativas < 5:
        # Pedir ao usuário para adivinhar o número
        palpite = int(input("Tentativa {}: Digite seu palpite: ".format(tentativas + 1)))
        
        # Verificar se o palpite está correto
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto!")
            return  # Sai da função
        elif palpite < numero_secreto:
            print("O número secreto é maior que o seu palpite.")
        else:
            print("O número secreto é menor que o seu palpite.")
        
        tentativas += 1
    
    # Se o usuário esgotar as tentativas
    print("Suas 5 tentativas acabaram! O número secreto era:", numero_secreto)

# Chamada da função para iniciar o jogo
jogo_adivinhacao()
