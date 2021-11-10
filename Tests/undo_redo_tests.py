from Domain.Book import BookOrder
from Logic.undo_redo import handle_undo, handle_redo, handle_new_list


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Ultima noapte...', 'Roman', 50, 'none'),
        BookOrder(5, 'Morometii', 'Roman', 35, 'silver')
    ]


def final_data_after_discount():
    return [
        BookOrder(1, 'Morometii', 'Roman', 33.25, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 18, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
    ]


def final_data_after_sort():
    return [
        BookOrder(3, 'Poezii', 'Lirica', 18, 'gold'),
        BookOrder(1, 'Morometii', 'Roman', 33.25, 'silver'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
    ]


def list_version_data():
    list_version = []
    before_discount = get_data()
    after_discount = final_data_after_discount()
    after_sort = final_data_after_sort()
    list_version.append(before_discount)
    list_version.append(after_discount)
    list_version.append(after_sort)
    return list_version


def test_undo():
    try:
        list_version = list_version_data()
        current_version = 1
        order_list = handle_undo(list_version, current_version)
        undo_test_list = final_data_after_discount()
        assert order_list == undo_test_list
    except AssertionError:
        print("Assertion Error")


def test_handle_new_list():
    try:
        list_version = list_version_data()
        current_version = 0
        new_order = get_data()
        list_version = handle_new_list(list_version, current_version, new_order)
        assert len(list_version) == 2
        assert new_order in list_version
    except AssertionError:
        print("Assertion Error")


def test_redo():
    try:
        list_version = list_version_data()
        current_version = 2
        order_list = handle_redo(list_version, current_version)
        redo_test_list = final_data_after_sort()
        assert order_list == redo_test_list
    except AssertionError:
        print("Assertion Error")


def test_redo_undo():
    test_undo()
    test_redo()
    test_handle_new_list()
