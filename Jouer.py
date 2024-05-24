from fonctions import reverse_list


class Play:
    def __init__(self, num_colonne, liste, joueur, nom1, type_motif1, type_motif2):
        self.num_colonne = num_colonne
        self.liste = liste
        self.joueur = joueur
        self.nom1 = nom1
        self.type_motif1 = type_motif1
        self.type_motif2 = type_motif2

    def jouer(self):
        global liste_change, type_motif, x
        if self.joueur == self.nom1:
            type_motif = self.type_motif1
        else:
            type_motif = self.type_motif2

        y = reverse_list(self.liste)
        j = self.num_colonne
        for i in range(len(y) - 1):
            l = y[i].split(" ")
            if l[j] == ".":
                l[j] = type_motif
                y[i] = " ".join(l)
                liste_change = reverse_list(y)
                x = "\n".join(liste_change)
                break
        print(x)


    def change_liste(self):
        return liste_change