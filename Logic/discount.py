
def apply_discount(order, discount):
    """
    The functions applies the proper discount to an order
    :param order: the order
    :param discount: the type of discount to be appliles
    :return:
            -the order after the discount was applied
            -the order if there is no discount to be applies
    """
    if discount == "silver":
        new_price = order.get_price() * 19/20
        order.change_price(new_price)
        return order
    if discount == "gold":
        new_price = order.get_price() * 9/10
        order.change_price(new_price)
        return order
    return order


def handle_discount(order_list):
    """
    The function handles the discounts for all the current orders
    :param order_list: the list of orders
    :return: the new list after the proper discounts were applied
    """
    if len(order_list) == 0:
        raise ValueError("The list is empty")
    new_list = []
    for order in order_list:
        discount = order.get_discount_type()
        new_order = apply_discount(order, discount)
        new_list.append(new_order)
    return new_list
