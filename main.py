"""
Scrieți un program pentru gestionarea unei librării. Vor fi suportate operațiile:
4.1. Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID
. O vânzare conține: ID, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
"""
from Tests.crud_tests import test_crud
from Tests.test_crud_list import test_crud_list
from Tests.test_crud_dict import test_crud_dict
from UserInterface.UI import run_ui
from UserInterface.UI_dict_list import run_ui


def main():
    order_list = []
    test_crud()
    # test_crud_list()
    test_crud_dict()
    # run_ui(order_list)
    run_ui(order_list)


main()
