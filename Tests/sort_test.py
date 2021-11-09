from Domain.Book import BookOrder
from Logic.sort import price_sort


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 40, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 30, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 50, 'none'),
    ]


def final_data():
    return [
        BookOrder(1, 'Poezii', 'Lirica', 20, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 30, 'none'),
        BookOrder(3, 'Morometii', 'Roman', 40, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 50, 'none'),
    ]


def test_price_sort():
    try:
        order = get_data()
        order = price_sort(order)
        final_order = final_data()
        assert order == final_order
    except AssertionError:
        print("Assertion error")
