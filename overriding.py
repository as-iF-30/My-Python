class Book:
    def __init__ (self,name,author):
        self.name = name
        self.author = author
    def __str__(self):
        print('{} by {}'.format(self.name, self.author))

class paperBook(Book):
    def __init__ (self,name, author, pnum):
        Book.__init__(self, name, author)
        self.pnum = pnum

class EBook(Book):
    def __init__ (self, name, author, size):
        Book.__init__(self, name, author)
        self.size = size

class Library:
    def __init__(self):
        self. books = []
    def addBook(self, book):
        self.books.append(book)
    def getNumBooks(self):
        return len(self.books)

mybook = EBook('The monk who sold his ferrari', 'robinsharma', 'A3')
myPaperBook = paperBook('Who will cry', 'Robin sharma', 123)

print(mybook.size)
print(myPaperBook.pnum)
o = Library()
o.addBook(mybook)
o.addBook(myPaperBook)
print(o.getNumBooks())
