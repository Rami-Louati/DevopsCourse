from math import cos
import seaborn as sns

def calculer_cosinus_sur_cent(valeur):
    return cos(valeur / 100)


if __name__ == "__main__":
    for i in range(314):
        print(cos(i / 10))
elif: 
    print("it was a good day")
