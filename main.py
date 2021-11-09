from Domain.Book import BookOrder
# from Logic.type_min_price import min_price
from Tests.crud_tests import test_crud
from Tests.discount_tests import test_discount
from Tests.sort_test import test_price_sort
from UserInterface.UI import run_ui


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Roman', 20, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
        BookOrder(5, 'Harap Alb', 'Basm', 35, 'gold'),
    ]


def main():
    order_list = get_data()
    test_crud()
    test_discount()
    test_price_sort()
    run_ui(order_list)
    # run_cli(order_list)


main()
