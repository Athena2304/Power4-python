import random
from Tableau import Tableau
from fonctions import *
from Jouer import *


def main():
    global nom1, nom2, type_motif1, type_motif2, liste, joueur, nombre_de_colonnes, nombre_de_lignes, type_motif

    nom1 = input("Entrez le nom du joueur 1 : ").strip()
    nom2 = input("Entrer le nom du joueur 2 : ").strip()
    effacer_le_terminal()

    print("Exemples de tableau (nombre de colonnes / nombre de lignes :\n * 7/6 (Classique)\n * 8/7\n * 8/8")
    nombre_de_colonnes = int(input("Entrer le nombre de colonnes : "))
    nombre_de_lignes = int(input("Entrer le nombre de lignes : "))
    effacer_le_terminal()
    tableau = Tableau(nombre_de_colonnes,nombre_de_lignes)



    print("Exemples de motifs: \n X : la croix \n O : le rond \n € : l'euro \n $ : le dollar")
    type_motif1 = input(f"{nom1},entrer le motif désiré : ").upper().strip()
    type_motif2 = input(f"{nom2},entrer le motif désiré : ").upper().strip()
    liste = tableau.liste()
    x = tableau.afficher(liste)
    print(x)

    premier_a_jouer = random.choice([nom1,nom2])
    num_colonne = int(input(f"{premier_a_jouer}, veuillez choisir une colonne : "))
    joueur = premier_a_jouer
    effacer_le_terminal()
    play = Play(num_colonne,liste,joueur,nom1,type_motif1,type_motif2)
    play.jouer()
    liste_change = play.change_liste()

    joueur = choix_du_joueur(joueur,nom1,nom2)
    num_colonne = int(input(f"{joueur}, veuillez choisir une colonne : "))
    effacer_le_terminal()
    play2 = Play(num_colonne, liste_change, joueur, nom1, type_motif1, type_motif2)
    play2.jouer()
    liste_change = play2.change_liste()
    it = condition_de_fin(liste_change,nombre_de_colonnes,type_motif1,joueur)

    while it == 0:
        joueur = choix_du_joueur(joueur,nom1,nom2)
        num_colonne = int(input(f"{joueur} , veuillez choisir une colonne : "))
        effacer_le_terminal()
        play2 = Play(num_colonne, liste_change, joueur, nom1, type_motif1, type_motif2)
        play2.jouer()
        liste_change = play2.change_liste()
        it = condition_de_fin(liste_change,nombre_de_colonnes,type_motif1,joueur)






demarrage = input("Voulez vous commencer la partie ? y/n : ").strip().lower()
if demarrage == "n":
    while demarrage == "n":
        print("On vous attend... ")
        demarrage = input("Voulez vous commencer la partie ? y/n : ").strip().lower()
effacer_le_terminal()
if __name__ == "__main__":
    main()

continuer = input("Voulez vous continuer ? y/n : ").strip().lower()
if continuer == "y":
    if __name__ == "__main__":
        main()
    while continuer == "y":
        continuer = input("Voulez vous continuer ? y/n : ").strip().lower()
        if __name__ == "__main__":
            main()

else:
    print("A la prochaine")
effacer_le_terminal()