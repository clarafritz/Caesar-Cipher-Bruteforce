# --------- FONCTIONS
def user_input(msg, decalage): 
    result = ''

    for charc in range(len(msg)):
        if msg[charc].isalpha():
            unicode = ord(msg[charc])
            position = ((unicode - 97) + decalage) % 26 
            charc_position = chr(97 + position)

            result += charc_position
        else: 
            result += msg[charc]

    return result


# ------------------------------------------------------
# --------- INTRODUCTION SCRIPT 
print('Bienvenue sur mon Script de Déchiffrement César')

# --------- PROGRAMME PRINCIPAL
msg = input("Veuillez saisir votre texte : ").lower()
decalage = int(input('Veuillez saisir votre decalage : '))

print(user_input(msg, decalage))
