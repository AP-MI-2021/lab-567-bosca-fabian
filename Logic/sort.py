def price_sort(order_list):
    """
    Sorts the current orders by price
    :param order_list: the list of orders
    :return: the sorted list
    """
    if len(order_list) == 0:
        raise ValueError("There are no orders to be sorted")
    return sorted(order_list, key=lambda x: x.price)
