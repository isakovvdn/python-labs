class Book:
    _id = 0

    def __init__(self, author, title):
        if not title:
            raise ValueError("Пустое название")

        self.author = author
        self.title = title
        self.code = None

    def set_code(self):
        Book._id += 1
        self.code = Book._id

    def tag(self):
        return [word for word in self.title.split() if word[0].isupper()]

    def __str__(self):
        author_short = self.author[0] + "." + self.author.split()[-1]
        return f"[{self.code}] {author_short} '{self.title}'"


class Library:
    def __init__(self, number, address):
        self.number = number
        self.address = address
        self.books = []

    def __iadd__(self, book):
        book.set_code()
        self.books.append(book)
        return self

    def __iter__(self):
        return iter(self.books)


lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')

for book in lib:
    print(book)
    print(book.tag())