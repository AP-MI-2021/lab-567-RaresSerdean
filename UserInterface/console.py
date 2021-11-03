from Logic.CRUD import AdaugareRezervare, StergeRezervare


def print_meniu():
    '''
    meniul de afisat
    '''

    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("x. Iesire")

def ui_adauga_rezervare(lst):
    '''
    Adauga o rezervare noua listei
    :param lst: lista de rezervari
    :return: lista de rezervari la care se adauga rezervarea nou introdusa
    '''

    try:
        ID = int(input("Dati ID-ul: "))
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati checkin-ul: ")
        return AdaugareRezervare(ID, nume, clasa, pret, checkin, lst)
    except ValueError as ve:
        print(f"Eroare : {ve}")
        return lst


def ui_sterge_rezervare(lst):
    '''
    Sterge o rezervare din lista
    :param lst: lista de rezervari
    :return: lista de rezervari la care se sterge o rezervare
    '''

    try:
        id_de_sters = int(input("Dati ID-ul rezervarii de sters: "))
        lst=StergeRezervare(id_de_sters,lst)
        return lst
    except ValueError as ve:
        print(f"Eroare:{ve}")
        return lst


def ui_modifica_rezervare(lst):
    '''
    Modifica o rezervare din lista
    :param lst: lista de rezervari
    :return: lista de rezervari la care se modifica o rezervare
    '''

    try:
        ID = int(input("Dati ID-ul: "))
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati checkin-ul: ")
        return ModificaRezervare(ID, nume, clasa, pret, checkin, lst)
    except ValueError as ve:
        print(f"Eroare:{ve}")
        return lst

def show_all(lst):
    '''
    afiseaza rezervarile din lista
    :param lst: lista de rezervari
    :return: rezervarile din lista afisate ca string
    '''
    for rezervare in lst:
        print(to_string(rezervare))


def run_menu(lst):
    while True:
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst=ui_adauga_rezervare(lst)
        elif optiune == "2":
            lst=ui_sterge_rezervare(lst)
        elif optiune == "3":
            lst=ui_modifica_rezervare()
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune invalida ! Reincercati")
