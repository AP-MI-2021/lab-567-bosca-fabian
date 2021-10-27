from Domain.Book import BookOrder


def create(order_list, book_id, title, book_type, price, discount):
    """
    The function adds a new order to the already existing list of orders
    :param order_list: The list that has all the current orders
    :param book_id: New order ID
    :param title: New order book title
    :param book_type: New order book type
    :param price: New order book price
    :param discount: New order type of discount
    :return: The list of orders with the new added order
    """
    book = BookOrder(book_id, title, book_type, price, discount)
    return order_list + [book]


def read(order_list, order_id):
    """
    The functions reads a specific order from the list of orders
    :param order_list: The list that has the current orders
    :param order_id: Order's that has to be read ID
    :return: The needed order
    """
    needed_order = None
    for order in order_list:
        if order.get_id() == order_id:
            needed_order = order
    return needed_order


def update(order_list, updated_order):
    """
    The function updates a list with the new details of an already existing order
    :param order_list: The list with the current orders
    :param updated_order: The update of an order
    :return: The new updated list
    """
    new_order_list = []

    for order in order_list:
        if order.get_id() == updated_order.get_id():
            new_order_list.append(updated_order)
        else:
            new_order_list.append(order)
    return new_order_list


def delete(order_list, order_id):
    """
    The functions deletes an order from the list of orders
    :param order_list: The current list of orders
    :param order_id: The order that has to be deleted ID
    :return: The new updated list
    """
    new_order_list = []
    for order in order_list:
        if order.get_id() != order_id:
            new_order_list.append(order)
    return new_order_list
