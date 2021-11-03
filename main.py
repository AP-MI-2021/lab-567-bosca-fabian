"""
Scrieți un program pentru gestionarea unei librării. Vor fi suportate operațiile:
4.1. Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID
. O vânzare conține: ID, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
"""
from Domain.Book import BookOrder
# from Logic.type_min_price import min_price
from Tests.crud_tests import test_crud
from Tests.discount_tests import test_discount
# from UserInterface.UI import run_ui
from UserInterface.cli import run_cli


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Roman', 20, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
    ]


def main():
    order_list = []
    test_crud()
    test_discount()
    # run_ui(order_list)
    run_cli(order_list)


main()
