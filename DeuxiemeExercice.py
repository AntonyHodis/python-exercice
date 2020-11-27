

def exercicePorteBonheur():

    #Fonction qui permet de faire le calcul
    def chiffrePorteNonheur(nb):
        
        #Initialisation d'une liste vide pour que cela soit plus simple à manipuler centaine,dizaine...
        L = []

        #On converti en chiffre pour que cela soit calculable et on met dans la liste centaine,dizaine.. 
        for i in nb:

            L.append(int(i))
            pass

        #on converti en int pour executer la boucle
        nb = int(nb)

        #Boucle jusqu'a inferieur 9
        while nb > 9:

            #Variable temporaire afin de securiser nb
            a = 0

            #On additionne les carrés de chaque argument d'une liste
            for l in L:

                a = a + l**2                
                pass
            
            #Mettre à jour nb pour peut être sortir de la liste
            nb = a

            #Conersion en string afin que le nombre puisse être une liste de caractere
            a = str(a)
            
            #Liste initialisé
            L = []

            #Remplissage de la liste en chiffre afin quelle puisse être calculé
            for i in a:

                
                L.append(int(i))

                pass

            pass

        #On retourne nb pour faire le test dans le programme pricipal
        return nb

    
    #On rentre notre chiffre pricipal
    nb = input("Rentre un chiffre : ")

    #Juste un texte afin de pas le copier 2 fois
    print("Le nombre {} est " .format(nb), end='')

    #Execution de la fonction pour dterminer si c'est un chiffre porte bonheur
    nb = chiffrePorteNonheur(nb)

    #On test si nb de base est un chiffre porte bonheur
    if nb == 1:

        print("un nombre porte bonheur !")

    else:

        print("n'est pas un nombre porte bonheur")       

    pass

def exerciceGeneG():

    #Fonction de notre générateur
    #@repet le nombre de fois que la lettre doit être crée
    #J'ai pas fait jusqu'à l'infini mais le principe est là
    def generateur(repet):

        for i in range(repet):

            yield 'a'
        
        for i in range(repet):

            yield 'b'
        
        for i in range(repet):

            yield 'c'

        for i in range(repet):

            yield 'd'

        for i in range(repet):

            yield 'e'
        
    
    #On crée notre variable g avec le nombre de lettre que l'on veut à chaque fois
    g = generateur(2)
    
    #On affiche le tout
    for a in g:

        print(a)

    

if __name__ == "__main__":

    exerciceGeneG()
    pass
