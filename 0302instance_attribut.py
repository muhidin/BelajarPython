class Pencil:
    def __init__(self):
        self.note = "I'm a pencil"

pencil1 = Pencil()
print("Object pencil1 note: ", pencil1.note)

class Book:
    note = "A class type to represent a book"

print(f"Class Book note: {Book.note}")

book1 = Book()
print(f"Object book1 note: {book1.note}")
# output ➜ Object book1 note: A class type to represent a book
