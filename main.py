"""
Scrieți un program pentru gestionarea unei librării. Vor fi suportate operațiile:
4.1. Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID
. O vânzare conține: ID, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
"""
from Tests.crud_tests import test_crud
from Tests.discount_tests import test_discount
from UserInterface.UI import run_ui


def main():
    order_list = []
    test_crud()
    test_discount()
    run_ui(order_list)


main()
