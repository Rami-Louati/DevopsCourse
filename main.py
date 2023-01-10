from math import cos


def calculer_cosinus_sur_cent(valeur):
    return cos(valeur / 100)


if __name__ == "__main__":
    for i in range(314):
        print(cos(i / 100))
