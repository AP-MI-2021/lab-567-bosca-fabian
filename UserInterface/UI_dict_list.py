# from Domain.Book_list import get_id, get_book_type, get_discount_type, get_title, get_price, create_order
from Logic.CRUD_list_dict import delete, create, read, update
from Domain.Book_dict import get_id, get_book_type, get_discount_type, get_title, get_price, create_order


def show_menu():
    print("""
1. Add new order
2. Delete order
3. Change order
4. Read a specific order
x. Exit
""")


def order_detail(order):
    return f'The order with the ID {get_id(order)} has the book called {get_title(order)}' \
           f'\nThe book type is {get_book_type(order)} and it has the price of {get_price(order)} RON' \
           f'\nThe current applied discount is {get_discount_type(order)}'


def show_order(order_list):
    order_id = int(input("Enter order ID to be shown: "))
    return order_detail(read(order_list, order_id))


def change_order(order_list):
    to_be_changed_id = int(input("Enter the order's ID you'd like to change: "))
    to_be_changed_title = input("Enter the order's new book: ")
    to_be_changed_type = input("Enter the order's new book type: ")
    to_be_changed_price = float(input("Enter the order's new book price: "))
    to_be_changed_discount = input("Enter the order's new book discount: ")
    new_order = create_order(to_be_changed_id, to_be_changed_title, to_be_changed_type,
                             to_be_changed_price, to_be_changed_discount)
    return update(order_list, new_order)


def add_new_order(order_list):
    book_id = int(input("Enter order ID: "))
    title = input("Enter book title: ")
    book_type = input("Enter book type: ")
    price = float(input("Enter book price: "))
    discount = input("Enter discount: ")
    return create(order_list, book_id, title, book_type, price, discount)


def delete_order(order_list):
    book_id = int(input("Enter order ID to be delete: "))
    return delete(order_list, book_id)


def run_ui(order_list):
    while True:
        show_menu()
        ui_command = input("Enter an option: ")
        if ui_command == '1':
            order_list = add_new_order(order_list)
            print(order_list)
        elif ui_command == '2':
            order_list = delete_order(order_list)
            print(order_list)
        elif ui_command == '3':
            order_list = change_order(order_list)
            print(order_list)
        elif ui_command == '4':
            print(show_order(order_list))
        elif ui_command == 'x':
            break
        else:
            print("Invalid command! Try again!")
