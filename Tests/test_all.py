from Tests.testCRUD import test_AdaugareRezervare, test_StergeRezervare, test_ModificaRezervare


def test_all():
    test_AdaugareRezervare()
    test_StergeRezervare()
    test_ModificaRezervare()