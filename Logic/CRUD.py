from Domain.Book import BookOrder
from UserInterface.UI_Logic import order_detail


def create(order_list, book_id, title, book_type, price, discount):
    book = BookOrder(book_id, title, book_type, price, discount)
    return order_list + [book]


def read(order_list, id):
    needed_order = None
    for order in order_list:
        if order.get_id() == id:
            needed_order = order
    return order_detail(needed_order)


def update(order_list, new_order):
    new_order_list = []

    for order in order_list:
        if order.get_id() == new_order.get_id():
            new_order_list.append(new_order)
        else:
            new_order_list.append(order)
    return new_order_list


def delete(order_list, book_id):
    new_order_list = []
    for order in order_list:
        if order.get_id() != book_id:
            new_order_list.append(order)
    return new_order_list
