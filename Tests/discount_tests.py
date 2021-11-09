from Domain.Book import BookOrder
from Logic.discount import apply_discount, handle_discount


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
    ]


def final_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 33.25, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 18, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
    ]


def test_apply_discount():
    order_list = get_data()
    order_0 = apply_discount(order_list[0], "silver")
    order_1 = apply_discount(order_list[1], "none")
    order_2 = apply_discount(order_list[2], "gold")
    order_3 = apply_discount(order_list[3], "none")
    try:
        assert order_0.get_price() == 33.25
        assert order_1.get_price() == 40
        assert order_2.get_price() == 18
        assert order_3.get_price() == 35
    except AssertionError:
        print("Assertion error")


def test_handle_discount():
    try:
        order_list = get_data()
        ordered_list = handle_discount(order_list)
        final_list = final_data()
        assert ordered_list == final_list
    except AssertionError:
        print("Assertion error")

def test_discount():
    test_apply_discount()
    test_handle_discount()
