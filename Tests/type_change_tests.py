from Domain.Book import BookOrder
from Logic.type_change import book_type_change


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Harap Alb', '', 50, 'none'),
    ]


def final_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 50, 'none'),
    ]


def test_book_type_change():
    try:
        order_list = get_data()
        given_title = "Harap Alb"
        given_type = "Basm"
        final_list = final_data()
        new_list = book_type_change(order_list, given_title, given_type)
        assert new_list == final_list
    except AssertionError as ae:
        print("Assertion Error", ae)
