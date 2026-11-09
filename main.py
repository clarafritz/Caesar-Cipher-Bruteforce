# --------- INTRODUCTION SCRIPT 
print('Bienvenue sur mon Script de Déchiffrement César')

# --------- CHOIX user
mot_user = input("Veuillez saisir un mot : ").lower()


# ----- FORCE BRUT : test des 26 décalages
for keys in range(26) : 
    mot_fini = ''
    
    for chrc in range(len(mot_user)) : 
        if mot_user[chrc].isalpha() : 
            # ------- TRANSFORMATION
            unicode = ord(mot_user[chrc])

            # ------- POSITIONNEMENT CESAR 
            position = ((unicode - 97) + keys) % 26
            chr_position = chr(97 + position)

            #--------- RESULTAT
            mot_fini += chr_position

        else: 
            mot_fini += mot_user[chrc]

    print('Apres déchiffrement, ', mot_user, " -> ", mot_fini, " avec la clé : ", keys)
        


