from Domain.Book import BookOrder
from Logic.CRUD import create, delete, update, read
from Logic.discount import handle_discount
from Logic.sort import price_sort
from Logic.type_change import book_type_change


def commands_help():
    print("""
To add an order use: add [id] [title] [type] [price] [discount]
To delete an order use: delete [id]
To change an order use: change [id] [title] [type] [price] [discount]
To show a specific order use: showspec [id]
To show all orders use: showall
To apply the discount to every order use: discount
To sort the current list based on price use: sort
To change the type of a title use: typechange [title] [type]
To show the help menu use: help
To exit use: exit

Types of discount currently available: none/silver/gold
Use ';' as a separator between commands
Use ' '{spacebar} as a separator within commands
""")


def run_change(order_list, params):
    book_id = int(params[0])
    if book_id < 0:
        raise ValueError("ID must be a positive integer")
    book_title = params[1]
    book_type = params[2]
    book_price = float(params[3])
    if book_price <= 0:
        raise ValueError("The book must have a price")
    book_discount = params[4]
    new_order = BookOrder(book_id, book_title, book_type, book_price, book_discount)
    return update(order_list, new_order)


def run_add(order_list, params):
    book_id = int(params[0])
    book_title = params[1]
    book_type = params[2]
    book_price = float(params[3])
    book_discount = params[4]
    return create(order_list, book_id, book_title, book_type, book_price, book_discount)


def run_cli(order_list):
    commands_help()
    stop = False
    while not stop:
        try:
            command_line = input("Enter all your commands:")
            command_line = command_line.split(';')
            for command in command_line:
                command = command.split()
                if command[0] == '':
                    pass
                elif command[0] == "exit":
                    print("You exited")
                    stop = True
                elif command[0] == 'showall':
                    if len(command[1:]):
                        raise ValueError("The correct command is: 'showall'")
                    print(order_list)
                elif command[0] == 'add':
                    if len(command[1:]) != 5:
                        raise ValueError("The correct command is: 'add [id] [title] [type] [price] [discount]'")
                    order_list = run_add(order_list, command[1:])
                elif command[0] == 'delete':
                    if len(command[1:]) != 1:
                        raise ValueError("The correct command is: 'delete [id]'")
                    order_list = delete(order_list, int(command[1]))
                elif command[0] == 'showspec':
                    if len(command[1:]):
                        raise ValueError("The correct command is: 'showspec'")
                    print(read(order_list, int(command[1])))
                elif command[0] == 'change':
                    if len(command[1:]) < 5:
                        raise ValueError("The correct command is: 'change [id] [title] [type] [price] [discount]'")
                    order_list = run_change(order_list, command[1:])
                elif command[0] == 'discount':
                    if len(command[1:]):
                        raise ValueError("The correct command is: 'discount'")
                    order_list = handle_discount(order_list)
                elif command[0] == 'sort':
                    if len(command[1:]):
                        raise ValueError("The correct command is: 'sort'")
                    order_list = price_sort(order_list)
                elif command[0] == 'typechange':
                    if len(command[1:]):
                        raise ValueError("The correct command is: 'typechange'")
                    order_list = book_type_change(order_list, command[1], command[2])
                elif command[0] == 'help':
                    if len(command[1:]):
                        raise ValueError("The correct command is: 'help'")
                    commands_help()
                else:
                    print(f"The command {command[0]} doensn't exist")
        except IndexError:
            pass
        except ValueError as ve:
            print(f"Error: {ve}")
