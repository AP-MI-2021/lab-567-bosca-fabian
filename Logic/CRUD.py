from Domain.Book import BookOrder


def create(order_list, order_id, title, book_type, price, discount):
    """
    The function adds a new order to the already existing list of orders
    :param order_list: The list that has all the current orders
    :param order_id: New order ID
    :param title: New order book title
    :param book_type: New order book type
    :param price: New order book price
    :param discount: New order type of discount
    :return: The list of orders with the new added order
    """
    types_of_discount = ["none", "silver", "gold"]
    if discount not in types_of_discount:
        raise ValueError("This type of discount doesn't exist")
    if order_id < 0:
        raise ValueError("ID must be a positive integer")
    if price <= 0:
        raise ValueError("The book must have a price")
    for already_existent_id in order_list:
        if already_existent_id.get_id() == order_id:
            raise ValueError("This ID already exists. Please enter another one!")

    book = BookOrder(order_id, title, book_type, price, discount)
    return order_list + [book]


def read(order_list, order_id):
    """
    The functions reads a specific order from the list of orders
    :param order_list: The list that has the current orders
    :param order_id: Order's that has to be read ID
    :return: The needed order
    """
    if len(order_list) == 0:
        raise ValueError("There are currently no orders!")
    needed_order = None
    for order in order_list:
        if order.get_id() == order_id:
            needed_order = order
    if needed_order is None:
        raise ValueError("No current order has the specified ID")
    return needed_order


def update(order_list, updated_order):
    """
    The function updates a list with the new details of an already existing order
    :param order_list: The list with the current orders
    :param updated_order: The update of an order
    :return: The new updated list
    """
    if len(order_list) == 0:
        raise ValueError("There are currently no orders!")
    types_of_discount = ["none", "silver", "gold"]
    discount = updated_order.get_discount_type()
    if discount not in types_of_discount:
        raise ValueError("This type of discount doesn't exist")
    new_order_list = []
    order_exists = False
    for order in order_list:
        if order.get_id() == updated_order.get_id():
            new_order_list.append(updated_order)
            order_exists = True
        else:
            new_order_list.append(order)
    if not order_exists:
        raise ValueError("There is no order with the specified ID")
    return new_order_list


def delete(order_list, order_id):
    """
    The functions deletes an order from the list of orders
    :param order_list: The current list of orders
    :param order_id: The order that has to be deleted ID
    :return: The new updated list
    """
    if len(order_list) == 0:
        raise ValueError("There are currently no orders!")
    new_order_list = []
    for order in order_list:
        if order.get_id() != order_id:
            new_order_list.append(order)
    if new_order_list == order_list:
        raise ValueError("No current order has the specified ID")
    return new_order_list
