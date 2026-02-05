class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("title is", self.title)
        print("author is", self.author)


class IssuedBook(Book):
    def __init__(self, issued_date, issued_to, title, author):
        super().__init__(title, author)
        self.issued_date = issued_date
        self.issued_to = issued_to

    def display_book_details(self):
        print(
            "title is", self.title,
            "and author is", self.author,
            "and issued date is", self.issued_date,
            "and issued to", self.issued_to
        )


child_object = IssuedBook(2021, "kadambari", "kannada", "jeevan")
child_object.display_book_details()
