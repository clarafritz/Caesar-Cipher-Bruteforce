# --------- FONCTIONS
def user_input(msg, decalage): 
    result = ''

    for charc in range(len(msg)):
        unicode = ord(msg[charc])

        if 65 <= unicode <= 90 or 97 <= unicode <= 122:
            if msg[charc].isupper():
                position = ((unicode - 65) + decalage) % 26 
                charc_position = chr(65 + position)
            else: 
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
option = input('Voulez-vous chiffrer (c) ou déchiffrer (d) votre message ? ')
msg = input("Veuillez saisir votre texte : ")
decalage = int(input('Veuillez saisir votre decalage : '))

if option == 'c' :
    print(user_input(msg, decalage))
elif option == 'd': 
    print(user_input(msg, -decalage))
else: 
    print('Vous avez choisi un mode inexistant')


