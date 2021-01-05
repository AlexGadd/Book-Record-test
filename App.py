# this handles saving and loading of files
from fileHandler import *
import time
import datetime


# Functions used within other functions
# takes input from a list of books and prints a list to choose from
def list_books(book_list, add_page_count_target=False):
    if not add_page_count_target:
        # creates a readable and selectable list of books passed from the database query
        for count, value in enumerate(book_list):
            current_book = f"{value[1]} by {value[2]}"
            print(f"{count + 1}. {current_book}")
    else:
        # adds page count target
        for count, value in enumerate(book_list):
            length = value[3]
            target_date = value[4]
            position = value[6]
            today = int(datetime.datetime.now().timestamp())
            pages_left = length - position
            days_left = int((target_date - today) / 86400)  # 86400 is the number of seconds in a day
            pages_per_day = int(pages_left / days_left)
            current_book = f'{value[1]} by {value[2]} -\t- read {pages_per_day} pages per day to meet your target'
            print(f"{count + 1}. {current_book}")


# function for listing all books with full info
def list_all_books():
    current = load_all()
    list_books(current)


# lists only the titles and author, used for making a list of books to choose from
def list_current_titles(add_page_count_target=False):
    current = load_current()
    if add_page_count_target:
        list_books(current, add_page_count_target)
    else:
        list_books(current)


# lists all finished books
def list_finished():
    current = load_finished()
    list_books(current)


# Overarching functions for parts of the main menu

# function for starting a new book
def new_book():
    book = [
        input("please enter a title: "),
        input("please enter the author's name: "),
        int(input("Please enter the number of pages: "))
            ]
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


def add_position():
    current_books = load_current()
    entered_position = False
    while not entered_position:
        print("Please choose a title:")
        list_current_titles(True)
        selection = int(0)
        try:
            selection = int(input())
            if len(current_books) >= selection > 0:
                selection = selection - 1
                this_book = current_books[selection]
                while True:
                    page_num = int(input("What page are you currently on?\n"))
                    if this_book[4] > page_num > 0:
                        rowid = str(current_books[selection][0])
                        add_new_position(rowid, page_num)
                        entered_position = True
                        break
                    elif page_num == this_book["length"]:
                        print("Congratulations, you've finished!")
                        rowid = str(current_books[selection][0])
                        change_to_complete(rowid)
                        entered_position = True
                        break
                    elif page_num == 0:
                        break
                    else:
                        print("Please enter a valid page number")
                break
            elif selection == 0:
                break
            else:
                print("Please enter a number corresponding with the books on the list")
        except:
            print("Please enter a number")


# main menu
def main_menu():
    stay = True
    choice = int(0)
    while stay:
        choice = int(0)
        try:
            print("\nWould you like to: ")
            print("1.Start a new book")
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


main_menu()
