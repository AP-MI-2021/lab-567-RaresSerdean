def CreeazaRezervare (ID, nume, clasa, pret, checkin):
    '''

    :param ID:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :return:
    '''
    lst=[('ID=',ID),('nume=',nume),('clasa=', clasa),('pret=',pret), ('checkin=',checkin)]
    return lst

def getid(rezervare):
    '''

    :param rezervare:
    :return:
    '''
    return rezervare[0] [1]

def getnume(rezervare):
    '''

    :param rezervare:
    :return:
    '''
    return rezervare[1] [1]

def getclasa(rezervare):
    '''

    :param rezervare:
    :return:
    '''
    return rezervare[2] [1]

def getpret(rezervare):
    '''

    :param rezervare:
    :return:
    '''

    return rezervare[3] [1]

def getcheckin(rezervare):
    '''

    :param rezervare:
    :return:
    '''

    return rezervare[4] [1]
