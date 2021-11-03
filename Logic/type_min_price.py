def get_all_book_types(order_list):
    """
    The functions finds all the book types
    :param order_list: the order list
    :return: new list of book types without dupllicates
    """
    new_list = []
    for types in order_list:
        if types.get_book_type() not in new_list:
            new_list.append(types.get_book_type())
    return new_list


def min_price(order_list):
    types_list = get_all_book_types(order_list)
    types_dictionary = {}

    for types in types_list:
        types_dictionary[types] = 0

    for books in order_list:
        book_type = books.get_book_type()
        book_price = books.get_price()
        if types_dictionary[books.get_book_type()] == 0:
            types_dictionary.update({book_type: book_price})
        else:
            if books.get_price() < types_dictionary[books.get_book_type()]:
                types_dictionary.update({book_type: book_price})

    return None


