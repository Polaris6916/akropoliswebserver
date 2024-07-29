from enum import Enum

#Enum des types de quartiers
class TypeQuartier(Enum):
    """Création de la classe TypeQuartier
    Permet d'associer un nom à une valeur numérique

    Args:
        Enum : Type de la classe (vient de la bibliotèque Enum)
    """
    Habitation = 1
    Marché = 2
    Caserne = 3
    Temple = 4
    Jardin = 5

# Classe Quartier définit par son niveau, son type et sa quantité
class Quartier:
    def __init__(self, type, niveau, nombre):
        """Constructeur de la class init

        Args:
            type (str): type de la structure (ex : Habitation, Marché...)
            niveau (int): De qu'elle niveau est le quartier (0,1,2..)
            nombre (int): Nombre de quartier en fonction du même type et même niveaux
        """
        self.Type = TypeQuartier(type)
        self.Niveau = int(niveau)
        self.Nombre = int(nombre)

    # Méthode permettant de calculer le score pour un quartier
    def Score(self):
        return self.Nombre * self.Niveau

# Classe Joueur
class Joueur:
    def __init__(self, nom):
        self.Nom = nom
        self.Pierres = 0
        self.Quartiers = [] #Liste des Quartiers par type & niveau
        self.Etoiles = 0

    # Méthode permettant de calculer le score d'un joueur
    def Score(self):
        scoreQuartiers = 0
        for quartier in self.Quartiers:
            scoreQuartiers += quartier.Score()
            
        return (self.Pierres + scoreQuartiers) * self.Etoiles

# Méthode obsolète permettant d'illuster l'implémentation de la logique d'utilisation
def main():
    # Création du premier joueur
    nomJoueur = input("Nom du joueur : ")
    joueur = Joueur(nomJoueur)

    # Saisie des caractéristiques de la ville du joueur
        # Pierres
    joueur.Pierres = int(input("Nombre de pierres : "))

        # Quartiers
    print("Description de vos quartiers")
    niveaux = int(input("\tQuel est votre niveau le plus élevé : "))

    for typeQuartier in TypeQuartier:
        print("\t\t",typeQuartier)
        for niveau in range(1, niveaux + 1):
            quantite = int(input("\t\tNiveau " + str(niveau) + " : "))
            if quantite > 0:
                nouveauQuartier = Quartier(typeQuartier, niveau, quantite)
                joueur.Quartiers.append(nouveauQuartier)

        # Etoiles
    joueur.Etoiles = int(input("Nombre d'étoiles : "))

    # Calcul du score du joueur
    scoreJoueur = joueur.Score()
    print()
    print(joueur.Nom, "votre score est : ", str(scoreJoueur))
    
def playerScore(username, stones, stars, quartiers):
    #Création du joueur via les donnée récupérée dans le formulaire web (pour son nom, son nombre de pierre et d'étoile)
    joueur = Joueur(username)
    joueur.Pierres = stones
    joueur.Etoiles = stars
    
    #Inscription des donnée quartier
    for i in range(len(quartiers)):
        niveau = int(quartiers[i][0])
        for j in range(1,6) :
            quantite = int(quartiers[i][j])
            typeQuartier = TypeQuartier(j)
            if quantite > 0 :
                nouveauQuartier = Quartier(typeQuartier, niveau, quantite)
                joueur.Quartiers.append(nouveauQuartier)
        
    return joueur.Score()

#Convertie la chaine de caractère quartier en un tableau
#Exemple : 1,1,2,0,4,10;2,0,0,0,0,0 donne [[1,1,2,0,4,10][2,0,0,0,0,0]]
def quartiersStrToArray(strQuartiers):
    arrQuartier = []
    
    rowsQuarier = strQuartiers.split(";")
    for i in range(len(rowsQuarier)):
        arrQuartier.append(rowsQuarier[i].split(","))
    
    return arrQuartier