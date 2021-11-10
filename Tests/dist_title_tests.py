from Domain.Book import BookOrder
from Logic.distinct_titles import dist_title, get_all_book_title


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Ultima noapte...', 'Roman', 50, 'none'),
        BookOrder(5, 'Morometii', 'Roman', 35, 'silver')
    ]


def final_data():
    return{"Roman": 2,
           "Nuvela": 1,
           "Lirica": 1
           }


def final_titles():
    return ["Morometii", "Moara cu noroc", "Poezii", "Ultima noapte..."]


def test_dist_title():
    try:
        order_list = get_data()
        final_dict = final_data()
        types_dict = dist_title(order_list)
        assert types_dict == final_dict
    except AssertionError as ae:
        print("Assertion Error", ae)


def test_get_all_book_titles():
    try:
        order_list = get_data()
        book_titles = get_all_book_title(order_list)
        final = final_titles()
        assert book_titles == final
    except AssertionError:
        print("Assertion Error")


def test_all_dist_titles():
    test_get_all_book_titles()
    test_dist_title()
