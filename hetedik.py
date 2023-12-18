import Renszarvas


def beolvas():
    lista = []
    beFajl = open("fajlok/Mikulasszan.txt", "r", encoding="utf-8")
    adatokListaja = beFajl.readlines()
    print(adatokListaja)
    for index in range(1, len(adatokListaja), 1):
        if not "Santa Claus" in adatokListaja[index]:
            daraboltSor = adatokListaja[index].split("@")
            szarvas = Renszarvas.Renszarvas(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
            # print(szarvas)
            lista.append(szarvas)
            # print(lista)
    beFajl.close()
    return lista


def angolMegfelelo(nev: str, lista: list):
    index = 0
    talalat = True
    while index < len(lista) and talalat:
        index += 1
        if lista[index].nevMagyar == nev:
            print(lista[index].nevAngol)
            talalat = False
    if not talalat:
        print(f"Szarvas angol neve: {lista[index].nevAngol}")
    else:
        print("Nincs ilyen rénszarvas.")
    """
    for szarvas in szarvasokListaja:
        if szarvas.nevMagyar == "Pompás":
            print(szarvas.nevAngol)
    """


def mikulasSzam(lista: list):
    db = 0
    index = 0
    while index < len(lista):
        daraboltLeiras = lista[index].leiras.split(" ")
        print(daraboltLeiras)
        index2 = 0
        while index2 < len(daraboltLeiras):
            if daraboltLeiras[index2] == "Mikulás":
                db += 1
            index2 += 1
        index += 1
    print(f"Mikulás szó előfordulásának száma: {db}")


def atlagMagassag(lista: list):
    osszeg = 0
    index = 0
    while index < len(lista):
        osszeg += lista[index].magassag
        index += 1
    if len(lista) == 0:
        print("Az átlag 0.")
    else:
        atlag = osszeg / len(lista)
        print(f"Az átlag: {atlag:.2f}")


def parosMagyar(lista: list):
    print("A páros helyen repülő szarvasok nevei: ", end="")
    index = 0
    while index < len(lista):
        if lista[index].hely % 2 == 0:
            print(lista[index].nevMagyar+" ", end="")
        index += 1
    print("")


def leghosszabbLeiras(lista: list):
    maxErtek = len(lista[0].leiras)
    maxIndex = 0
    index = 1
    while index < len(lista):
        if len(lista[index].leiras) > maxErtek:
            maxErtek = len(lista[index].leiras)
            maxIndex = index
        index += 1
    print(f"A leghosszabb leírás: {lista[maxIndex].nev}, (hossza: {maxErtek} karakter")


def hetes():
    # alap feladat
    szarvasokListaja = beolvas()
    # a feladat
    for szarvas in szarvasokListaja:
        print(szarvas.kiir())
    # b feladat
    print(f"Rénszarvasok száma: {len(szarvasokListaja)}")
    angolMegfelelo("Pompás", szarvasokListaja)
    mikulasSzam(szarvasokListaja)
    atlagMagassag(szarvasokListaja)
    parosMagyar(szarvasokListaja)
    leghosszabbLeiras(szarvasokListaja)
