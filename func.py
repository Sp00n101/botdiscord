import random
n=5
mass = []
c=1/n


def picture():
    mass = []
    c = 1 / n
    q = c
    while q <= 1:
        mass.append(q)
        q=q+c
    ran = random.random()
    if ran < mass[0]:
        return "1.jpg"
    if ran > mass[0] and ran < mass[1]:
        return "2.jpg"
    if ran > mass[1] and ran < mass[2]:
        return "3.jpg"
    if ran > mass[2] and ran < mass[3]:
        return "4.jpg"
    if ran > mass[3] and ran < 1:
        return "5.jpg"

