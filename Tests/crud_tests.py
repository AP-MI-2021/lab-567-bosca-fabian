from Domain.Book import BookOrder
from Logic.CRUD import create, update, read, delete


def get_data():
    return [
        BookOrder(1, 'Morometii', 'Roman', 35, 'silver'),
        BookOrder(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        BookOrder(3, 'Poezii', 'Lirica', 20, 'gold'),
        BookOrder(4, 'Harap Alb', 'Basm', 35, 'none'),
    ]


def test_create():
    try:
        vanzari = get_data()
        params = (5, 'Franklin', 'Copii', 43, 'none')
        new_vanzare = create(vanzari, *params)
        assert len(new_vanzare) == len(vanzari) + 1
    except AssertionError:
        print("Assertion Error")


def test_read():
    try:
        vanzari = get_data()
        some_v = vanzari[2]
        assert read(vanzari, some_v.get_id()) == some_v
    except AssertionError:
        print("Assertion Error")


def test_instance(v_updated, v_list):
    for instance in v_list:
        if v_updated.get_id() == instance.get_id():
            if instance == v_updated:
                return 1
    return 0


def test_update():
    try:
        vanzari = get_data()
        v_updated = BookOrder(3, 'Geronimo Stilton', 'Copii', 60, 'gold')
        updated = update(vanzari, v_updated)
        assert test_instance(v_updated, updated) == 1
        assert test_instance(v_updated, vanzari) == 0
        assert len(updated) == len(vanzari)
    except AssertionError:
        print("Assertion Error")


def test_delete():
    try:
        vanzari = get_data()
        to_delete = 3
        deleted = delete(vanzari, to_delete)
        assert len(deleted) == len(vanzari) - 1
    except AssertionError:
        print("Assertion Error")


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
