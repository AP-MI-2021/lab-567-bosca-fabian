def create_order(book_id, book_title, book_type, price, discount):
    return {
        "book_id": book_id,
        "book_title": book_title,
        "book_type": book_type,
        "price": price,
        "discount": discount,
    }


def get_id(order):
    return order["book_id"]


def get_title(order):
    return order["book_title"]


def get_book_type(order):
    return order["book_type"]


def get_price(order):
    return order["price"]


def get_discount_type(order):
    return order["discount"]


def order_detail(order):
    return f'The order with the ID {get_id(order)} has the book called {get_title(order)}' \
           f'\nThe book type is {get_book_type(order)} and it has the price of {get_price(order)} RON' \
           f'\nThe current applied discount is {get_discount_type(order)}'
