# from Domain.Book_list import create_order, get_id
from Domain.Book_dict import create_order, get_id


def create(order_list,
           order_id: int, book_title: str, book_type: str, price: float, discount: str):
    """
   The function adds a new order to the already existing list of orders
   :param order_list: The list that has all the current orders
   :param order_id: New order ID
   :param book_title: New order book title
   :param book_type: New order book type
   :param price: New order book price
   :param discount: New order type of discount
   :return: The list of orders with the new added order
   """
    order = create_order(order_id, book_title, book_type, price, discount)
    return order_list + [order]


def read(order_list, order_id):
    """
   The functions reads a specific order from the list of orders
   :param order_list: The list that has the current orders
   :param order_id: Order's that has to be read ID
   :return: The needed order
   """
    check_order = None
    for order in order_list:
        if get_id(order) == order_id:
            check_order = order

    if check_order:
        return check_order
    return order_list


def update(order_list, new_order):
    """
   The function updates a list with the new details of an already existing order
   :param order_list: The list with the current orders
   :param new_order: The update of an order
   :return: The new updated list
   """
    new_list = []
    for order in order_list:
        if get_id(order) != get_id(new_order):
            new_list.append(order)
        else:
            new_list.append(new_order)

    return new_list


def delete(order_list, order_id):
    """
   The functions deletes an order from the list of orders
   :param order_list: The current list of orders
   :param order_id: The order that has to be deleted ID
   :return: The new updated list
   """
    new_list = []
    for order in order_list:
        if get_id(order) != order_id:
            new_list.append(order)
    return new_list
