class BookOrder:

    ID = 0
    book_title = ""
    book_type = ""
    price = 0
    discount_type = ""

    def __init__(self, _id, _book_title, _book_type, _price, _discount_type):
        self.ID = _id
        self.book_title = _book_title
        self.book_type = _book_type
        self.price = _price
        self.discount_type = _discount_type

    def change_price(self, new_price):
        self.price = new_price

    def get_id(self):
        return self.ID

    def get_book_title(self):
        return self.book_title

    def get_book_type(self):
        return self.book_type

    def get_price(self):
        return self.price

    def get_discount_type(self):
        return self.discount_type

    def __str__(self):
        return f'ID = {self.ID}; Title = {self.book_title}; Type = {self.book_type}; ' \
               f'Price = {self.price}; Discount = {self.discount_type}'

    def __repr__(self):
        return str(self)
