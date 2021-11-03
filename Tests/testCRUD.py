from Domain.rezervare import getid, getnume, getclasa, getpret, getcheckin
from Logic.CRUD import AdaugareRezervare, getbyid, StergeRezervare, ModificaRezervare


def test_AdaugareRezervare():
    lst=[]
    lst=AdaugareRezervare(1,'Popescu Andrei', 'Economy plus', 800, 'Da', lst)

    assert len(lst) == 1
    assert getid(getbyid(1, lst)) == 1
    assert getid(getbyid(1, lst))


def test_StergeRezervare():
    lst=[]
    lst = AdaugareRezervare(2, 'Maria Ana', 'Economy', 600, 'Da', lst)
    lst = AdaugareRezervare(3, 'Popescu Andrei', 'Economy plus', 800, 'Da', lst)
    lst = StergeRezervare(3,lst)

    assert len(lst) == 1
    assert getbyid(3, lst) is None
    assert getbyid(2, lst) is not None


def test_ModificaRezervare():
    lst=[]
    lst = AdaugareRezervare(2, 'Maria Ana', 'Economy', 600, 'Da', lst)
    lst = AdaugareRezervare(3, 'Popescu Andrei', 'Economy plus', 800, 'Da', lst)
    lst = ModificaRezervare(2, 'Camelia Morar', 'Business', 1000, 'Da', lst)
    assert len(lst) == 2
    RezervareModificata = getbyid(2, lst)

    assert getid(RezervareModificata) == 2
    assert getnume(RezervareModificata) == 'Camelia Morar'
    assert getclasa(RezervareModificata) == 'Business'
    assert getpret(RezervareModificata) == 1000
    assert getcheckin(RezervareModificata) == 'Da'

    RezervareNemodificata = getbyid(3, lst)
    assert getid(RezervareNemodificata) == 3
    assert getnume(RezervareNemodificata) == 'Popescu Andrei'
    assert getclasa(RezervareNemodificata) == 'Economy plus'
    assert getpret(RezervareNemodificata) == 800
    assert getcheckin(RezervareNemodificata) == 'Da'





