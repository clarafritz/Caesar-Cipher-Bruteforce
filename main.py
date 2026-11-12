# --------- FONCTIONS
# Fonction qui chiffre / déchiffre un msg avec un décalage précis 
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



# Fonction : attaque par force brut : test les 26 clés grâce la fonction user_input()
def brute_force(msg): 
    for key in range(26):
        print('key (', key, ') : ', user_input(msg, key))




# ------------------------------------------------------
# --------- INTRODUCTION SCRIPT 
print('==== CAESAR CIPHER ====')

# --------- PROGRAMME PRINCIPAL
option = input(
    'Choisissez votre option : \n' 
    '   c --> chiffrement \n' 
    '   d --> dechiffrement \n' 
    '   b --> attaque par force brute \n'
    'Votre choix : '
)
msg = input("Message à analyser : ")


if option == 'b':
    brute_force(msg)
elif option == 'c' or option == 'd':
    decalage = int(input('Veuillez saisir votre decalage : '))

    if option == 'c' :
        print(user_input(msg, decalage))
    else:
        print(user_input(msg, -decalage))
        
else: 
    print('Vous avez choisi un mode inexistant')


