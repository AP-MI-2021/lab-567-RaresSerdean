from Domain.rezervare import CreeazaRezervare, getid


def AdaugareRezervare(ID, nume, clasa, pret, checkin, lst):
    rezervare=CreeazaRezervare(ID, nume, clasa, pret, checkin)
    return lst+[rezervare]


def getbyid(ID, lst):
    for rezervare in lst:
        if getid(rezervare) == ID:
            return rezervare

def StergeRezervare(ID, lst):
    rezultat=[]
    for rezervare in lst:
        if getid(rezervare) != ID:
            rezultat.append(rezervare)
    return rezultat


def ModificaRezervare(ID, nume, clasa, pret, checkin, lst):
    rezultat=[]
    for rezervare in lst:
        if getid(rezervare) == ID:
            RezervareNoua=CreeazaRezervare(ID, nume, clasa, pret, checkin)
            rezultat.append(RezervareNoua)
        else:
            rezultat.append(rezervare)
    return rezultat

