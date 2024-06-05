while True:
    senha = input("Digite sua senha: ")
    tem_numero = False
    tem_letra = False
    
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue
    
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        elif caractere.isalpha():
            tem_letra = True
    
    if not (tem_numero and tem_letra):
        print("A senha deve conter tanto números quanto letras.")
        continue
    
    print("Senha válida!")
    break
