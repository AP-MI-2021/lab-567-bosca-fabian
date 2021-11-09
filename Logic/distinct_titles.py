from Logic.type_min_price import get_all_book_types


def get_all_book_title(order_list: list):
    """
    The functions finds all the book titles
    :param order_list: the order list
    :return: new list of book titles without dupllicates
    """
    new_list = []
    for types in order_list:
        if types.get_book_title() not in new_list:
            new_list.append(types.get_book_title())
    return new_list


def dist_title(order_list: list):
    """
    The functions finds the numbers of distinct titles for each book type
    :param order_list: the list of orders
    :return: a dictionary in which key : value is book_type : number of distinct titles
    """
    if not len(order_list):
        raise ValueError("There are no current orders")
    types_list = get_all_book_types(order_list)
    title_list = get_all_book_title(order_list)
    types_dictionary = {}

    for types in types_list:
        types_dictionary[types] = 0

    for books in order_list:
        book_type = books.get_book_type()
        book_title = books.get_book_title()
        if book_title in title_list:
            types_dictionary[book_type] += 1
            title_list.remove(book_title)

    return types_dictionary
