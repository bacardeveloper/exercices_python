import os

class SubScorpion:
    def __init__(self) -> None:
        pass
    
    def afficher_chemin(self):
        commande = "ls"
        valeur_retour = os.system(commande)
        print(valeur_retour)

def main():
    print(' demarrage ')
    sub_scorpion = SubScorpion()
    sub_scorpion.afficher_chemin()
    
if __name__ == "__main__":
    main()