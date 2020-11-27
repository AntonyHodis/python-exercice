

def exercicePorteBonheur():

    def chiffrePorteNonheur(nb):

        L = []

        for i in nb:

            L.append(int(i))
            pass

        nb = int(nb)

        while nb > 9:

            a = 0

            for l in L:

                a = a + l**2

                
                pass
            
            nb = a
            a = str(a)
            
            L = []

            for i in a:

                
                L.append(int(i))

                pass

            pass

        return nb

    

    nb = input("Rentre un chiffre : ")

    print("Le nombre {} est " .format(nb), end='')

    nb = chiffrePorteNonheur(nb)

    if nb == 1:

        print("un nombre porte bonheur !")

    else:

        print("n'est pas un nombre porte bonheur")       

    pass

def exerciceGeneG():

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
        
    

    g = generateur(2)
    
    for a in g:

        print(a)

    

if __name__ == "__main__":

    exerciceGeneG()
    pass
