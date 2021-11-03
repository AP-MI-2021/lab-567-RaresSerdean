from Tests.test_all import test_all
from UserInterface.console import run_menu, print_meniu


def main():
    test_all()
    lst=[]
    print_meniu()
    run_menu(lst)

if __name__=='__main__':
    main()