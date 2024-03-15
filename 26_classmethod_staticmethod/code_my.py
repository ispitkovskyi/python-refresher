# Way to implementing factory using 'static-methods' instead of 'class-methods'
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @staticmethod
    def hardcover_static(name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @staticmethod
    def paperback_static(name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


heavy = Book.hardcover_static("Harry Potter", 1500)
light = Book.paperback_static("Python 101", 600)

print(heavy)
print(light)
