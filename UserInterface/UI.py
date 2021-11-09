from copy import deepcopy

from Domain.Book import BookOrder
from Logic.CRUD import delete, create, read, update
from Logic.distinct_titles import dist_title
from Logic.type_change import book_type_change
from Logic.discount import handle_discount
from Logic.sort import price_sort
from Logic.type_min_price import min_price
from Logic.undo_redo import handle_new_list, handle_undo, handle_redo


def show_crud_menu():
    print("""
1. Add new order
2. Delete order
3. Change order
4. Read a specific order
x. Exit
""")


def show_menu():
    print("""
1. Crud options
2. Apply discount
3. Change book type
4. Minimum price for every book type
5. Sort orders by price
6. Show number of distinct titles of all types
a. Show all the current orders

Undo
Redo

x. Exit""")


def order_detail(order):
    return f'The order with the ID {order.get_id()} has the book called {order.get_book_title()}' \
           f'\nThe book type is {order.get_book_type()} and it has the price of {order.get_price()} RON' \
           f'\nThe current applied discount is {order.get_discount_type()}'


def show_order(order_list):
    try:
        order_id = int(input("Enter order ID to be shown: "))
        needed_order = read(order_list, order_id)
        return order_detail(needed_order)
    except ValueError as ve:
        print("Error:", ve)
    return order_list


def show_dist_title(number_of_dist_titles):
    for key, value in number_of_dist_titles.items():
        print(f'For the book type {key}, the number of distinct titles is {value}')
    return


def change_order(order_list):
    try:
        to_be_changed_id = int(input("Enter the order's ID you'd like to change: "))
        if to_be_changed_id < 0:
            raise ValueError("ID must be a positive integer")
        to_be_changed_title = input("Enter the order's new book: ")
        to_be_changed_type = input("Enter the order's new book type: ")
        to_be_changed_price = float(input("Enter the order's new book price: "))
        if to_be_changed_price <= 0:
            raise ValueError("The book must have a price")
        to_be_changed_discount = input("Enter the order's new book discount(none/silver/gold): ")
        new_order = BookOrder(to_be_changed_id, to_be_changed_title, to_be_changed_type,
                              to_be_changed_price, to_be_changed_discount)
        return update(order_list, new_order)
    except ValueError as ve:
        print("Error", ve)
    return order_list


def add_new_order(order_list):
    try:
        book_id = int(input("Enter order ID: "))
        title = input("Enter book title: ")
        book_type = input("Enter book type: ")
        price = float(input("Enter book price: "))
        discount = input("Enter discount(none/silver/gold): ")
        return create(order_list, book_id, title, book_type, price, discount)
    except ValueError as ve:
        print("Error:", ve)
    return order_list


def delete_order(order_list):
    try:
        book_id = int(input("Enter order ID to be delete: "))
        return delete(order_list, book_id)
    except ValueError as ve:
        print("Error", ve)
    return order_list


def crud_ui(order_list):
    stop = False
    while not stop:
        show_crud_menu()
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
            stop = True
        else:
            print("Invalid command! Try again!")
    return order_list


def show_min_price(min_price_dict):
    for key, value in min_price_dict.items():
        print(f'For the book type {key}, the minium price is {value}')
    return


def handle_book_type_change(order_list):
    try:
        given_title = input("Name the title of the book you want to have type changed:")
        given_type = input("Name the new type:")
        order_list = book_type_change(order_list, given_title, given_type)
    except ValueError as ve:
        print("Error:", ve)
    return order_list


def run_ui(order_list):
    stop = False
    list_versions = [deepcopy(order_list)]

    current_version = 0
    while not stop:
        show_menu()
        ui_command = input("Enter an option: ")
        if ui_command == '1':
            order_list = crud_ui(order_list)
            list_versions = deepcopy(handle_new_list(list_versions, current_version, order_list))
        elif ui_command == '2':
            order_list = handle_discount(order_list)
            list_versions = deepcopy(handle_new_list(list_versions, current_version, order_list))
            current_version += 1
            print(order_list)
        elif ui_command == '3':
            order_list = handle_book_type_change(order_list)
            list_versions = deepcopy(handle_new_list(list_versions, current_version, order_list))
            current_version += 1
            print(order_list)
        elif ui_command == '4':
            type_min_price = min_price(order_list)
            show_min_price(type_min_price)
        elif ui_command == '5':
            order_list = price_sort(order_list)
            list_versions = deepcopy(handle_new_list(list_versions, current_version, order_list))
            current_version += 1
            print(order_list)
        elif ui_command == '6':
            nr_dist_title = dist_title(order_list)
            show_dist_title(nr_dist_title)
        elif ui_command == 'a':
            print(order_list)
        elif ui_command == 'Undo':
            try:
                current_version -= 1
                order_list = handle_undo(list_versions, current_version)
            except ValueError as ve:
                current_version += 1
                print("Error:", ve)
        elif ui_command == 'Redo':
            try:
                current_version += 1
                order_list = handle_redo(list_versions, current_version)
            except ValueError as ve:
                current_version -= 1
                print("Error:", ve)
        elif ui_command == 'x':
            stop = True
        else:
            print("Invalid command! Try again!")
