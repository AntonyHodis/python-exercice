from math import pi, sqrt
from random import randint
from itertools import permutations


def exo1():
    nom_utilisateur = input("Saisi ton nom : ")

    print("Bienvenue " + nom_utilisateur + " !")


def exo2():
    valeur1 = int(input("Saisi le premier nombre : "))
    valeur2 = int(input("Saisi le deuxieme nombre : "))

    print(str(valeur1) + " + " + str(valeur2) + " = " + str(valeur1 + valeur2))


def exo3():

    valeur1 = int(input("Saisi le premier nombre : "))
    valeur2 = int(input("Saisi le deuxieme nombre : "))
    if valeur1 > valeur2:
        print(str(valeur1) + " est superieur a " + str(valeur2))
    else:
        print(str(valeur2) + " est superieur a " + str(valeur1))


def exo4():

    valeur1 = int(input("Saisi un nombre : "))

    if valeur1 % 2 == 0:
        print("Le chiffre " + str(valeur1) + " est pair")
    else:
        print("Le chiffre " + str(valeur1) + " est impair")


def exo5():

    valeur1 = int(input("Saisi ton age : "))

    if valeur1 >= 18:
        print("Vous etes majeur !")
    else:
        print("Vous etes mineur")


def exo6():

    valeur1 = int(input("Saisi le premier nombre : "))
    valeur2 = int(input("Saisi le deuxieme nombre : "))
    valeur3 = int(input("Saisi le troisieme nombre : "))

    maximum = valeur1

    if valeur2 > maximum:
        maximum = valeur2

    if valeur3 > maximum:
        maximum = valeur3

    print("Le chiffre maximum est " + str(maximum))


def exo7():

    for i in range(101):
        print(str(i))


def exo8():

    valeur1 = int(input("Saisi un nombre : "))
    total = 0

    for i in range(1, valeur1 + 1):
        total = total + i

    print("La somme est : " + str(total))


def exo9():

    valeur1 = int(input("Saisi un nombre : "))
    total = 1

    for i in range(1, valeur1 + 1):
        total = total * i

    print("La valeur factorielle est : " + str(total))


def exo10():

    valeur1 = float(input("Saisi le rayon du cercle : "))
    perimetre = float(2) * pi * valeur1
    aire = pi * valeur1**float(2)

    print("Ton cercle a un rayon de " + str(valeur1) +
          " , un perimetre de {:.2f}" .format(perimetre) + " et un aire de {:.2f}" .format(aire))


def exo11():

    valeur1 = int(input("Saisi un nombre : "))

    for i in range(1, valeur1+1):
        if valeur1 % i == 0:
            print(i)


def exo12():

    for i in range(1, 10):

        for y in range(11):

            print(str(i) + " x " + str(y) + " = " + str(i*y))
            pass
        print()
        pass


def exo13():

    valeur1 = int(input("Saisi le premier nombre : "))
    valeur2 = int(input("Saisi le deuxieme nombre : "))

    print("Le quotient est " + str(valeur1/valeur2) +
          " et le reste est " + str(valeur1 % valeur2))


def exo14():

    valeur1 = int(input("Saisi un nombre : "))

    if sqrt(valeur1) % 1 == 0:
        print("C'est un carre parfait")
    else:
        print("Ce n'est pas un carre parfait")


def exo15():

    valeur1 = int(input("Saisi un nombre : "))
    compte = 0

    for i in range(1, valeur1+1):

        if valeur1 % i == 0:
            compte += 1
            # print(i)
        pass

    if compte == 2:
        print("Le nombre " + str(valeur1) + " est un nombre premier")
        pass
    else:
        print("Le nombre " + str(valeur1) + " n'est pas un nombre premier")
        pass


def exo16():

    s = "Python"
    tabChar = list(s)

    for i in tabChar:
        print(i + " ", end='')


def exo17():

    s = "itescia.fr"

    tabChar = list(s)

    for c in tabChar:

        print("Le caractère : \"{}\" figure {} fois dans la chaine s" .format(
            c, tabChar.count(c)))


def exo18():

    s = input("Saisi un mot : ")

    for i in s:
        if s[i] == 'a':
            print("La lettre 'a' se trouve à la position : {}" .format(i))
            pass
        pass


def exo19():

    l = ("laptop", "iphone", "tablet")

    for s in l:
        print(len(s))
        pass
    pass


def exo20():

    s = input("Saisi un mot : ")
    tabchar = list(s)

    taille = len(s)

    temp = tabchar[taille - 1]

    tabchar[taille - 1] = tabchar[0]
    tabchar[0] = temp

    s = ''.join(tabchar)

    print(s)


def exo21():

    s = "anticonstitutionellement"
    voyelle = ("aeiouy")

    compte = 0

    for c in s:
        for v in voyelle:
            if c == v:
                compte += 1

    print("La chaine \"{}\" possede {} voyelles" .format(s, compte))


def exo22():

    t = "Python est un merveilleux langage de programmation"

    tabS = t.split(" ")
    print(tabS[0])


def exo23():

    s = input("Saisi un fichier avec extension : ")

    tabS = s.split(".")
    print("L'extension du fichier est .{}" .format(tabS[len(tabS) - 1]))


def exo24():

    s = input("Saisi un mot : ")
    inverse = "".join(reversed(s))

    if s == inverse:
        print("Le mot {} est un palindrome" .format(s))
    else:
        print("Le mot {} n'est pas un palindrome" .format(s))


def exo25():

    s = input("Saisi un mot : ")
    inverse = "".join(reversed(s))

    print(inverse)


def exo26():

    s = input("Saisi un texte : ")

    tabS = s.split(" ")

    for s in tabS:
        if s[0] == 'a':
            print(s)


def exo27():

    s = input("Ecris n'importe quoi : ")

    motLong = ''

    tabS = s.split(" ")

    for mot in tabS:
        if len(mot) > len(motLong):
            motLong = mot

    print("Le mot le plus long est {} avec {} lettres" .format(motLong, len(motLong)))


def exo28():

    s = ''
    if not s:
        print("La chaine de caractere est vide")
    else:
        print("La chaine de caractere n'est pas vide")


def exo29():

    liste = ["tartiflette", "raclette", "fondue", "tartiflette", "chorizo"]
    liste = set(liste)

    print(liste)


def exo30():

    liste1 = ["velo", "trotinette", "gant", "broche"]
    liste2 = ["broche", "grille", "spray", "mouchoir", "ordinateur", "velo"]

    for s in liste1:
        for y in liste2:
            if y == s:
                print("Le mot {} est en commun" .format(y))


def exo31():

    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    listepair = []
    listeImpair = []

    for i in liste:
        if i % 2 == 0:
            listepair.append(i)
        else:
            listeImpair.append(i)

    print("Liste pair : {} \nListe impair : {}" .format(listepair, listeImpair))


def exo32():

    liste = [0, 1, 2, 3]

    liste1 = list(permutations(liste))
    print(liste1)


def exo33():

    s = "Python"
    t = ""

    for i in range(len(s)):
        # print(s[i])
        if i % 2 == 0:
           # print(s[i])
            t = t + s[i]

    print(t)


def exo34():

    liste = []
    liste1 = []
    for i in range(20):
        liste.append(randint(0, 20))

    for i in liste:
        if i >= 10:
            liste1.append(i)

    print(liste1)


def exo35():

    dico = {}

    s = input("Ecris n'importe quoi : ")

    liste = s.split(" ")

    for mot in liste:
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1

    for i in dico.items():
        print(i)
        pass
    pass


def exo36():

    s = input("Ecris n'importe quoi avec multiples espace : ")

    s = ' '.join(s.split())

    print(s)
    pass


def exo37():

    liste1 = ("banane", "fraise", "pomme", "chocolat", "grenade", "kiwi")
    liste2 = ("raisin", "fraise", "mangue", "orange",
              "clementine", "pomme", "banane")

    liste1 = set(liste1)
    liste2 = set(liste2)

    liste3 = set(liste1 & liste2)

    print(liste3)
    pass


def exo38():

    s = input("Ecris n'importe quoi : ")

    liste = s.split()

    liste[0], liste[len(liste) - 1] = liste[len(liste) - 1], liste[0]

    s = " ".join(liste)

    print(s)

    pass


def exo39():

    s = input("Ecris n'importe quoi : ")

    liste = s.split()

    print("Dans la chaine s, il y a {} mots" .format(len(liste)))

    pass


def exo41():

    def nombreDivisibles(liste, n):

        listeDivisible = []
        i = 0

        for chiffre in liste:

            if chiffre % n == 0:

                listeDivisible.append(chiffre)
                i += 1
                pass
            pass

        return listeDivisible, i

    liste = []

    for i in range(20):
        liste.append(randint(0, 8000))
        pass

    n = randint(0, 12)
    listeDivisible, i = nombreDivisibles(liste, n)

    print("Il y a {} éléments dans la liste {} qui sont divisibles par {} \nLa voici {}" .format(
        i, liste, n, listeDivisible))
    pass


def exo42():

    def nombreOccurences(L, x):

        i = 0

        for element in L:

            if element == x:
                i += 1
                pass
            pass

        return i

    liste = []

    for i in range(20):
        liste.append(randint(0, 10))
        pass

    i = randint(0, 10)

    print("Il y a {} occurences dans la liste {} avec le chiffre {}" .format(
        nombreOccurences(liste, i), liste, i))

    pass


def exo43():

    def insertEtoile(s):

        return "*".join(s)

    print(insertEtoile("Python"))

    pass


def exo44():

    def toutEnMajuscule(L):

        L2 = []

        for mot in L:

            L2.append(mot.upper())
            pass

        return L2

    L = ["Python", "est", "un", "langage", "de", "programmation"]
    L = toutEnMajuscule(L)

    print(L)
    pass


def exo45():

    def minMaj(s):

        minuscule = 0
        majuscule = 0

        s = s.replace(" ", '')

        for c in s:

            if c.isupper():
                majuscule += 1
            else:
                minuscule += 1

        return minuscule, majuscule

    s = input("Ecris n'importe quoi : ")

    minuscule, majuscule = minMaj(s)

    print("Dans la chaine s, il y a {} minuscules et {} majuscules" .format(
        minuscule, majuscule))
    pass


def exo46():

    def etablirChiffre(n):

        L = []

        while n != 0:

            L.append(n % 10)
            n = int(n / 10)
            pass
        L.reverse()

        return L

    n = int(input("Rentre un nombre : "))
    print("La liste de ton nombre : {} " .format(etablirChiffre(n)))
    pass


def exo47():

    def getMotCommun(T1, T2):

        T1 = T1.split()
        T2 = T2.split()

        T1 = set(T1)
        T2 = set(T2)
        L = set(T1 & T2)
        L = list(L)
        

        return L

    T1 = ("Python est un langage de programmation")
    T2 = ("Python est orienté objet")

    print("Les mots commun entre les 2 listes sont : {}" .format(
        getMotCommun(T1, T2)))
    pass


if __name__ == "__main__":
    exo47()
