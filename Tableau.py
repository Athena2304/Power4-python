class Tableau:
    def __init__(self, nombre_de_colonnes,nombre_de_lignes):
        self.nombre_de_colonnes = nombre_de_colonnes
        self.nombre_de_lignes = nombre_de_lignes

    def liste(self):
        global liste
        liste = []
        x = ""
        for i in range(1, self.nombre_de_colonnes + 1):
            x += " " + str(i)
        liste.append(x)
        for j in range(self.nombre_de_lignes):
            x = " "
            for i in range(self.nombre_de_colonnes):
                x += ". "
            liste.append(x)
        return liste

    def afficher(self,liste):
        x = "\n".join(liste)
        return x