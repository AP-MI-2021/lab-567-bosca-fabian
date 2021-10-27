from Domain.Book_dict import create_order, get_id
from Logic.CRUD_list_dict import create, read, update, delete


def get_data():
    return [
        create_order(1, "ion", "lectura", 100, "none"),
        create_order(2, "Baltag", "actiue", 70, "silver"),
        create_order(3, "Ana", "Drama", 20, "gold"),
        create_order(4, "Povesti", "lectura", 48, "none"),
    ]


def test_create():
    book_list = get_data()
    new_book = create_order(5, "Baltagul", "comedie", 50, "none")
    new_list = create(book_list, 5, "Baltagul", "comedie", 50, "none")
    assert len(new_list) == len(book_list)+1


def test_read():
    book_list = get_data()
    random_book = book_list[2]
    assert read(book_list, get_id(random_book)) == random_book


def test_update():
    book_list = get_data()
    new_book = create_order(3, "Baltagul", "camedie", 51, "none")
    new_list = update(book_list, new_book)
    assert len(new_list) == len(book_list)


def test_delete():
    book_list = get_data()
    id_delete = 3
    deleted_book = read(book_list, id_delete)
    new_list = delete(book_list, id_delete)
    assert len(new_list) == len(book_list)-1
    assert deleted_book not in new_list


def test_crud_dict():
    test_create()
    test_read()
    test_update()
    test_delete()
