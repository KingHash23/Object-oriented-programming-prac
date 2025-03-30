class Author:
    def __init__(self,name,nationality):
        self.name =name
        self.nationality = nationality
class Book(Author):
    def __init__(self,name,nationality,title,genre,availability):
        super().__init__(name,nationality)
        self.title = title
        self.genre = genre
        self.availability = availability
    def borrow_book(self):
        #handle cases where a book is borrowed already
        if self.availability:
            print("This book is already borrowed.")
        else:
            self.availability = True
            print(f"The book {self.title} has been borrowed.")
        return True
    def display_book(self):
        print(f"Title: {self.title}\nAuthor: {self.name}\nNationality: {self.nationality}\nGenre: {self.genre}\nAvailability: {'Available' if self.availability else 'Not Available'}")
        return True
    #instances
book1 = Book("John Doe","English","The Great Gatsby","Fiction",True)
book2 = Book("Jane Doe","French","Le Petit Prince","Fiction",False)
book3 = Book("Bob Smith","Spanish","El Senor de los Anillos","Fantasy",True)
    #borrowing a book
book1.borrow_book()
    #displaying a book
book1.display_book()
    #trying to borrow a book already borrowed
book1.borrow_book()
    #displaying a book
book1.display_book()
    #returning a book
book1.availability = False
book1.borrow_book()