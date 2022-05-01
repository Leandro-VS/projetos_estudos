"""Gerador Automatico de Senhas
"""

# Imports
import random
import string

def password_generator(len_pass=8):
    """Gera uma senha aleatória

    Args:
        len_pass (int, optional): Qunatidade de Digitos. Defaults to 8.

    Returns:
        string: senha aleatoria
    """    
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    
    password_user = ''
    for digit in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

# Armazena a resposta do usuário
choice_user = input("Quantos digitos para a senha?\n")

# Verifica entrada do usuario
if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()

# Retorna a senha para o usuario
response = password_generator(len_pass=choice_user)
print(f"Senha gerada:\n {response}")