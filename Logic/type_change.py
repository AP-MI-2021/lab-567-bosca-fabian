def book_type_change(order_list: list, book_title: str, book_type: str):
    """
    The functions handles the changes of book types for a given title
    :param order_list: the order list
    :param book_title: the title of the type to be changed
    :param book_type: the new type
    :return: the new list with changed type
    """
    if len(order_list) == 0:
        raise ValueError("There are currently no book orders!")
    new_list = []
    book_exist = False
    for book in order_list:
        if book.get_book_title() == book_title:
            book_exist = True
            book.change_type(book_type)
            new_list.append(book)
        else:
            new_list.append(book)
    if not book_exist:
        raise ValueError("There are no books with the given title")
    return new_list
