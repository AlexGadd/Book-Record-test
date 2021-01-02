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
        Book.bookID += 1

    def get_id_num(self):
        return str(self.bookID).zfill(4)

    def __lt__(self, other):
        return self.bookID < other.bookID

    def __str__(self):
        return(f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.length}\nTarget finish date: {self.target_date}\nCurrently Reading? {'Yes' if self.current else 'No'}")

    def get_book_name(self):
        return(f"{self.title} by {self.author}")

#exit checker should exit the application
##removed for now##

#function for starting a new book
def new_book():
    objBooks.append(Book(input("please enter a title: "), input("please enter the author's name: "), int(input("Please enter the number of pages: ")), input("please enter the target date: ")))
    print(objBooks[len(objBooks)-1].__dict__)
    books.append(objBooks[len(objBooks)-1].__dict__)
    print(books)
    save(books)

#function for listing all books with full info
def list_all_books():
    for x in books:
        print(x)

#function for listing all current books
def list_current_books():
    filtered_list = [item for item in books if item.get('current') == True]
    if filtered_list:
        return filtered_list
    else:
        print("You don't have any books that you're currently")

#lists only the titles and author, used for making a list of books to choose from
def list_titles():
    for count, value in enumerate(books):
        currentBook = f"{value['title']} by {value['author']}"
        print(f"{count + 1}. {currentBook}")

def add_position():
    enteredPosition = False
    while not enteredPosition:
            print("Please choose a title:")
            list_titles()
            selection = 0
            try:
                selection = int(input())
                print(selection)
                if selection <= len(books):
                    selection = selection -1
                    thisBook = books[selection]
                    while True:
                        pageNum = int(input("What page are you currently on?\n"))
                        if pageNum < thisBook["length"] and pageNum > 0:
                            books[selection]["position"] = pageNum
                            save(books)
                            enteredPosition = True
                            break
                        elif pageNum == thisBook["length"]:
                            print("Congratulations, you've finished!")
                            thisBook["position"] = pageNum
                            thisBook["current"] = False
                            save(books)
                            enteredPosition = True
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
                new_book()
            elif choice == 2:
                add_position()
            elif choice == 3:
                pass
            elif choice == 0:
                stay = False
        except:
            if choice =='exit':
                break
            print("\n\n!Please enter a number between 1 and 3!")

mainMenu()
