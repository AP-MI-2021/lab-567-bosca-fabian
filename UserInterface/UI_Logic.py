
def show_menu():
    print("""
1. Add new order
2. Delete order
3. Change order
4. Read a specific order
x. Exit
""")

def order_detail(order):
    return f'The order with the ID {order.get_id()} has the book called {order.get_book_title()}' \
           f'\nThe book type is {order.get_book_type()} and it has the price of {order.get_price()} RON' \
           f'\nThe current applied discount is {order.get_discount_type()}'


"""
TODO
De scapat de logica circulara!!!
DE CE TREBE SA FAC UN ALT FISIER SA IMI MEARGA???????????????????????????????????????//

"""