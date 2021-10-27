def create_order(book_id: int, book_title: str, book_type: str, price: float, discount: str):

    return [book_id, book_title, book_type, price, discount]


def get_id(order):
    return order[0]


def get_title(order):
    return order[1]


def get_book_type(order):
    return order[2]


def get_price(order):
    return order[3]


def get_discount_type(order):
    return order[4]


def order_detail(order):
    return f'The order with the ID {get_id(order)} has the book called {get_title(order)}' \
           f'\nThe book type is {get_book_type(order)} and it has the price of {get_price(order)} RON' \
           f'\nThe current applied discount is {get_discount_type(order)}'
