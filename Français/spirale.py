import time

def generer_spirale(taille):
    spirale = [[0] * taille for _ in range(taille)]  # Création d'une grille carrée

    x, y = taille // 2, taille // 2  # Départ au centre
    num = 1
    dx, dy = 0, -1

    for _ in range(taille * taille):
        if 0 <= x < taille and 0 <= y < taille:
            spirale[y][x] = num
            num += 1

        # Calcul des nouvelles coordonnées
        nx, ny = x + dx, y + dy

        # Changement de direction si on sort du cadre ou si la case est déjà remplie
        if not (0 <= nx < taille and 0 <= ny < taille and spirale[ny][nx] == 0):
            dx, dy = -dy, dx  # Rotation à droite
            nx, ny = x + dx, y + dy

        x, y = nx, ny  # Mise à jour des coordonnées

    return spirale

def afficher_spirale_avec_animation(spirale):
    taille = len(spirale)
    affichage = [[" " for _ in range(taille)] for _ in range(taille)]  # Tableau vide

    for y in range(taille):
        for x in range(taille):
            affichage[y][x] = f"{spirale[y][x]:02d}"  # Formatage des nombres

            # Affichage progressif
            for ligne in affichage:
                print(" ".join(ligne))
            time.sleep(0.1)
            print("\n" * 5)  # Effet de rafraîchissement

# Demande de l'utilisateur
taille = int(input("Saisissez la largeur de la spirale (impair) : "))
if taille % 2 == 0:
    print("Veuillez entrer un nombre impair.")
else:
    spirale = generer_spirale(taille)
    afficher_spirale_avec_animation(spirale)
