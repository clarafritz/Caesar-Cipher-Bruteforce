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


# Fonction : analyse caractere + calcule % de chaque lettre présente
def frequency_analysis(msg):
    alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
        'z': 0
    }

    msg = msg.lower()
    total_lettre = 0
    mot_analyser = {}

    for lettre in msg: 
        if lettre.isalpha() and lettre.isascii():
            alphabet[lettre] += 1
            total_lettre += 1

    if total_lettre == 0:
        print('Aucune lettre valide à analyser')
        return mot_analyser 

    for lettre, occ in alphabet.items():
        if occ != 0:
            frequence = (occ / total_lettre) * 100
            mot_analyser[lettre.upper()] = round(frequence, 2)
            print(f"Lettre : {lettre.upper()} | Occurrences : {occ} | Fréquence : {round(frequence, 2)}%")

    return mot_analyser




# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# Tableau de référence francaise : fréquence moyenne approximative des lettres utilisées
average_frequency = {
    'A': 8.15, 'B': 0.97, 'C': 3.15, 'D': 3.73, 'E': 17.39,
    'F': 1.12, 'G': 0.97, 'H': 0.85, 'I': 7.31, 'J': 0.45,
    'K': 0.02, 'L': 5.69, 'M': 2.87, 'N': 7.12, 'O': 5.28,
    'P': 2.80, 'Q': 1.21, 'R': 6.64, 'S': 8.14, 'T': 7.22,
    'U': 6.38, 'V': 1.64, 'W': 0.03, 'X': 0.41, 'Y': 0.28,
    'Z': 0.15
}

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


frequency_analysis(msg)