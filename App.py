# this handles saving and loading of files
from fileHandler import *
import os
import time
import datetime

# temporary fix for files being saved in wrong place
if not "Book Record test" in os.getcwd():
    os.chdir("/Users/alex/Desktop/playground/Python/Book Record test")

# Variables



# exit checker should exit the application
##removed for now##

# function for starting a new book
def new_book():
    book = []
    book.append(input("please enter a title: "))
    book.append(input("please enter the author's name: "))
    book.append(int(input("Please enter the number of pages: ")))
    print("Please enter the target date")
    year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))
    date = f"{day}/{month}/{year}"
    date = datetime.datetime.strptime(date, "%d/%m/%Y")
    date = date.timetuple()
    date = time.mktime(date)
    book.append(int(date))
    book.append(str(True))
    book.append(0)
    book = tuple(map(str, book))
    save(book)


# function for listing all books with full info
def list_all_books():
    current = load_all()
    for count, value in enumerate(current):
        current_book = f"{value[1]} by {value[2]}"
        print(f"{count + 1}. {current_book}")


# lists only the titles and author, used for making a list of books to choose from
def list_current_titles():
    current = load_current()
    for count, value in enumerate(current):
        current_book = f"{value[1]} by {value[2]}"
        print(f"{count + 1}. {current_book}")


def add_position():
    current_books = load_current()
    entered_position = False
    while not entered_position:
        print("Please choose a title:")
        list_current_titles()
        selection = 0
        try:
            selection = int(input())
            print(selection)
            if selection <= len(current_books):
                selection = selection - 1
                this_book = current_books[selection]
                while True:
                    page_num = int(input("What page are you currently on?\n"))
                    if page_num < this_book[4] and page_num > 0:
                        rowid = str(current_books[selection][0])
                        add_new_position(rowid,page_num)
                        entered_position = True
                        break
                    elif page_num == this_book["length"]:
                        print("Congratulations, you've finished!")
                        rowid = str(current_books[selection][0])
                        change_to_complete(rowid)
                        entered_position = True
                        break
                    else:
                        print("Please enter a valid page number")
                break
            else:
                print("Please enter a number corresponding with the books on the list")
        except:
            print("Please enter a number")


# main menu
def mainMenu():
    stay = True
    choice = int(0)
    while stay:
        choice = int(0)
        try:
            print("\nWould you like to: ")
            print("1. Start a new book")
            print("2.Add a new page position to a book you're reading")
            print("3.View stats on a previously read book?")
            choice = input()
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
            if choice == 'exit':
                break
            print("\n\n!Please enter a number between 1 and 3!")


mainMenu()
