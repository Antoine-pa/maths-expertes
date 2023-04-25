from turtle import *
from math import pi, cos, sin
from math import gcd

def get_text(text: str, n: int, k: int, angle_rad: float) -> str:
    """
    Fonction qui donne la valeur du point à afficher
    entrées :
        - text : la forme du nombre à afficher
        - n : la racine n-ieme
        - k : la valeur du point
        - angle_rad : la valeur de l'angle à afficher
    sortie :
        renvoie le texte à afficher
    """
    t = ""
    if text in ("algébrique", "algé"):
        a = round(cos(angle_rad), 2)
        b = round(sin(angle_rad), 2)
        if b == 0:
            t = f"{a}"
        elif a == 0:
            t = f"{b}i"
        elif b < 0:
            t = f"{a}{b}i"
        else:
            t = f"{a}+{b}i"
        t = "  "+t
    elif text in ("exponentielle", "exp", "polaire", "pol", "trigonométrique", "trigo"):
        a = 2*k
        b = n
        pgcd = gcd(a, b)
        if pgcd != 0:
            a //= pgcd
            b //= pgcd
        if a == 0:
            t = "0"
        elif b == 1 and a == 1:
            t = "π"
        elif b == 1:
            t = f"{a}π"
        elif a == 1:
            t = f"π/{b}"
        else:
            t = f"{a}π/{b}"

        if text in ("polaire", "pol"):
            t = f"  (1, {t})"
        elif text in ("exponentielle", "exp"):
            if t == "0":
                t = "  1"
            elif t == "π":
                t = "  -1"
            else:
                t = f"  e^i{t}"
        else:
            t = f"  cos({t})+isin({t})"
    return t


def poly_reg(pos: tuple, size: int, n: int, cercle: bool = True, text:str = None, point: bool = True) -> None:
    """
    Fonction qui trace un polygone régulier avec les racines n-ième de l'unité
    entrées :
        - pos (x, y) : la position du polygone dans l'espace
        - size : la taille du polygone
        - n : le nombre de racine
        - cercle : l'affichage ou non du cercle
        - text : l'affichage ou non des valeurs des racines
    """
    if cercle:
        #affichage du cercle
        up()
        goto(pos[0], pos[1] - size)
        down()
        circle(size)
    up()
    if text is not None:
        goto(pos[0] - size-50, pos[1] + size+10)
        write(f"racines {n}-ieme de l'unitée")
        goto(pos[0] - size-50, pos[1] + size)
        write("type de coordonnées : "+text)
    goto(pos[0], pos[1])
    if point:
        dot(5)
    if text is not None:
        write("  0")
    goto(pos[0]+size, pos[1]) #on se positionne au début du polygone
    down()
    for k in range(0, n):
        angle_rad = (2*k*pi)/n #l'angle en radiant du point
        x = cos(angle_rad)*size+pos[0] #la position du point en x
        y = sin(angle_rad)*size+pos[1] #en y
        goto(x, y) #on se déplace aux coordonnées de la prochaine racine
        if point:
            dot(6)
        if text is not None:
            #afichage de la valeur de la racine
            write(get_text(text, n, k, angle_rad))
    goto(pos[0]+size, pos[1]) #on revient au point de départ

def aprox_circle(n, pos=(0, 0), radius=200):
    """
    Fonction donnant une approximation d'un cercle
    entrées :
        - n : le nombre de segments du cercle
        - pos : la position du centre du cercle
        - radius : le rayon du cercle
    """
    poly_reg(pos, radius, n, False, None, False)


def display_racine_n_ieme():
    """
    Fonction qui affiche les racines n-ième de l'unité
    """
    n = int(input("équation de type w^n=1 n : "))
    rayon = 200
    poly_reg(pos = (-40, 30), size = rayon, n = n, cercle = True, text = "exponentielle", point = True)


reset()
setup(600, 500)

#aprox_circle(100)
display_racine_n_ieme()

done()
