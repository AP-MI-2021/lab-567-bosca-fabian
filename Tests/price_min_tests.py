from Domain.Book import BookOrder
from Logic.type_min_price import min_price, get_all_book_types


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Ultima noapte...', 'Roman', 50, 'none'),
    ]


def final_data():
    return {"Roman": 35,
            "Nuvela": 40,
            "Lirica": 20}


def final_types():
    return ["Roman", "Nuvela", "Lirica"]


def test_book_types():
    try:
        order_list = get_data()
        book_types = get_all_book_types(order_list)
        final = final_types()
        assert final == book_types
    except AssertionError:
        print("Assertion Error")


def test_min_price():
    try:
        order_list = get_data()
        dict_min_price = min_price(order_list)
        final_dict = final_data()
        assert dict_min_price == final_dict
    except AssertionError as ae:
        print("Assertion Error", ae)


def test_all_min_price():
    test_min_price()
    test_book_types()
