class Book:
    bookID = 0
    def __init__(self, title, author, length, target_date):
        self.bookID = Book.bookID
        self.title = title
        self.author = author
        self.length = length
        self.target_date = target_date
        self.current = True
        self.position = 0
        Book.bookID +=1

    def getIdNum(self):
        return str(self.bookID).zfill(4)
    
    def __lt__(self, other):
        return self.bookID < other.bookID

    def bookInfo(self):
        return("Title: " + self.title + "\nAuthor: " + self.author + "\nNumber of pages: " + self.length + "\nTarget finish date: " + self.target_date + "\nCurrently Reading? " + "Yes" if self.current else "No")

book1 = Book(input("please enter a title: "), input("please enter the author's name: "), input("Please enter the number of pages"), input("please enter the target date"))

print(book1.bookInfo())

# choice = input("Would you like to: \n1. Start a new book\n2.Add a new page position to a book you're reading\n3.View stats on a previously read book?\n")
# "\nCurrent position: " + self.position +