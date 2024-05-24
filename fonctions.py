import os

def choix_du_joueur(joueur,nom1,nom2):
    if joueur == nom1:
        joueur = nom2
    else :
        joueur = nom1
    return joueur
def effacer_le_terminal():
    if os.name == "nt" or os.name == "dos":
        command = "cls"
    else:
        command = "clear"

    os.system(command)


def reverse_list(liste: list) -> list:
    new_list = []
    longueur = len(liste)
    for i in range(longueur-1, -1, -1):
        new_list.append(liste[i])
    return new_list


def condition_de_fin(liste_change,nombre_de_colonnes,type_motif,joueur):
    global it
    it = 0
    if "." not in liste_change[1]:
        it=1

    for i in range(1, len(liste_change)):
        for j in range(1, nombre_de_colonnes + 1):
            if liste_change[i][j] == type_motif:
                try:
                    if liste_change[i][j] == liste_change[i][j + 2] == liste_change[i][j + 4] == liste_change[i][j + 6]:
                        it=2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i][j - 2] == liste_change[i][j] == liste_change[i][j + 2] == liste_change[i][j + 4]:
                        it= 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i][j - 4] == liste_change[i][j - 2] == liste_change[i][j] == liste_change[i][j + 2]:
                        it = 1
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i][j - 6] == liste_change[i][j - 4] == liste_change[i][j - 2] == liste_change[i][j]:
                        it = 2
                        break
                except IndexError:
                    None


                try:
                    if liste_change[i][j] == liste_change[i + 1][j] == liste_change[i + 2][j] == liste_change[i + 3][j]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i - 1][j] == liste_change[i][j] == liste_change[i + 1][j] == liste_change[i + 2][j]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i - 2][j] == liste_change[i - 1][j] == liste_change[i][j] == liste_change[i + 1][j]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i - 3][j] == liste_change[i - 2][j] == liste_change[i - 1][j] == liste_change[i][j]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i][j] == liste_change[i + 1][j + 2] == liste_change[i + 2][j + 4] == liste_change[i + 3][j + 6]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i - 1][j - 2] == liste_change[i][j] == liste_change[i + 1][j + 2] == liste_change[i + 2][j + 4]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i - 2][j - 4] == liste_change[i - 1][j - 2] == liste_change[i][j] == liste_change[i + 1][j + 2]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i - 3][j - 6] == liste_change[i - 2][j - 4] == liste_change[i - 1][j - 2] == liste_change[i][j]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i][j] == liste_change[i - 1][j + 2] == liste_change[i - 2][j + 4] == liste_change[i - 3][j + 6]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i + 1][j - 2] == liste_change[i][j] == liste_change[i - 1][j + 2] == liste_change[i - 2][j + 4]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i + 2][j - 4] == liste_change[i + 1][j - 2] == liste_change[i][j] == liste_change[i - 1][j + 2]:
                        it = 2
                        break
                except IndexError:
                    None
                try:
                    if liste_change[i + 3][j - 6] == liste_change[i + 2][j - 4] == liste_change[i + 1][j - 2] == liste_change[i][j]:
                        it = 2
                        break
                except IndexError :
                    None
    if it == 1:
        print("Vous avez tous les deux perdus")
    elif it == 2:
        print(f"{joueur}, vous avez gagné")
    else:
        None

    return it
