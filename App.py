#this handles saving and loading of files
from fileHandler import *
import os

#temporary fix for files being saved in wrong place
if not "Book Record test" in os.getcwd():
    os.chdir("/Users/alex/Desktop/playground/Python/Book Record test")

#Variables
books = load()
objBooks = []



#Main book class
class Book:
    bookID = len(books)
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

#exit checker should exit the application 
##removed for now##

#function for starting a new book
def newBook():
    objBooks.append(Book(input("please enter a title: "), input("please enter the author's name: "), int(input("Please enter the number of pages: ")), input("please enter the target date: ")))
    print(objBooks[len(objBooks)-1].__dict__)
    books.append(objBooks[len(objBooks)-1].__dict__)
    print(books)
    save(books)

#function for listing all books with full info
def listAllBooks():
    for x in books:
        print(x)

#lists only the titles and author, used for making a list of books to choose from
def listTitles():
    for count, value in enumerate(books):
        currentBook = f"{value['title']} by {value['author']}"
        print(f"{count + 1}. {currentBook}")

def addPosition():
    while True:
            print("Please choose a title:")
            listTitles()
            selection = 0
            try:
                selection = int(input())
                if selection <= (len(books)-1):
                    print("this works")
                    selection = selection -1
                    thisBook = books[selection]
                    while True:
                        pageNum = input("What page are you currently on?")
                        if pageNum < thisBook["length"] and pageNum < 0:
                            thisBook["position"] = pageNum
                            save(books)
                            break
                        elif pageNum == thisBook["position"]:
                            print("Congratulations, you've finished!")
                            thisBook["position"] = pageNum
                            thisBook["current"] = False
                            save(books)
                            break
                        else:
                            print("Please enter a valid page number")
                    break
                else:
                    print("Please enter a number corresponding with the books on the list")
            except:
                print("Please enter a number")




                



#main menu
def mainMenu():
    stay = True
    choice = int(0)
    while stay:
        choice = int(0)
        try:
            choice = input("\nWould you like to: \n1. Start a new book\n2.Add a new page position to a book you're reading\n3.View stats on a previously read book?\n")
            choice = int(choice)
            if choice == 1:
                newBook()
            elif choice == 2:
                addPosition()
            elif choice == 3:
                pass
            elif choice == 0:
                stay = False
        except:
            if choice =='exit':
                break
            print("\n\n!Please enter a number between 1 and 3!")

mainMenu()
