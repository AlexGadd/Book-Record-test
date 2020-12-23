books = []
stay = True

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

    def __str__(self):
        return(f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.length}\nTarget finish date: {self.target_date}\nCurrently Reading? {'Yes' if self.current else 'No'}")

    def getBookName(self):
        return(f"{self.title} by {self.author}")

def exitchecker(answer):
    typed = input(answer)
    if typed == "exit" or typed == 0:
        stay = False
        exit()
    else:
        return typed




def newBook():
    books.append(Book(exitchecker("please enter a title: "), exitchecker("please enter the author's name: "), exitchecker("Please enter the number of pages: "), exitchecker("please enter the target date: ")))

def listAllBooks():
    for x in books:
        print(x)

def listTitles():
    print("Please choose a title:")
    for count, value in enumerate(books):
        print(f"{count + 1}. {value.getBookName()}")



def mainMenu():
    choice = 0
    while stay:
        try:
            choice = int(exitchecker("\nWould you like to: \n1. Start a new book\n2.Add a new page position to a book you're reading\n3.View stats on a previously read book?\n"))
        except:
            print("\n\n!Please enter a number between 1 and 3!")

        if choice == 1:
            newBook()
        elif choice == 2:
            listTitles()
        elif choice == 3:
            pass


mainMenu()