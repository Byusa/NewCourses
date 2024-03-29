# Callable Objects

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("Outliers", "Malcolm Gladwell", 39.95)
b2 = Book("Think and grow rich", "Napoleon Hill", 29.95)

# TODO: call the object as if it were a function
print(b1)
b1("A thousands hills", "Stephen Kenzer", 49.95)
print(b1)