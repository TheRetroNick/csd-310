#    Nicholas Schmid
#    Assignment 12.3
#    WhatABook: Delivery

import sys
import mysql.connector
from mysql.connector import errorcode

# Database config object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Show Start Menu
def show_menu():
    print("\n  -- Table of Contents (Main Menu)-- \n")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program\n")

    try:
        choice = int(input('      <Example enter: 1 for book listing>: '))
        return choice

    # Return to Main Menu if invalid entry
    except ValueError:
        print("\n  Invalid entry, go fish.\n")
        sys.exit()


# Join the books and users to wishlists
def show_books(_cursor):

    # Inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")

    # Show the book information
    for book in books:
        print("  Book ID Number: {}\n  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2], book[3]))

# Show location
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

# Validate user ID 
def validate_user():

    try:
        user_id = int(input('\n      Enter a customer id \n      <Example 1 for user_id 1>: '))

        # If the selected user doesn't exist
        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, please start over.\n")
            sys.exit()

        return user_id

    # Stop program for invalid input.
    except ValueError:
        print("\n  Invalid entry, go fish.\n")
        sys.exit()

# Show User Menu
def show_account_menu():


    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))

        return account_option
    
    # Exit if invalid input
    except ValueError:
        print("\n  That's not a valid number. That wasn't even a number. Try again.\n")

        sys.ext()

def show_wishlist(_cursor, _user_id):
    # List the books to add to wishlist

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    # Show the wishlist
    wishlist = _cursor.fetchall()
    print("\n        -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    
    # Show the books not in the users wishlist
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)

    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

# Add the book to the wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # Try/catch block for handling potential MySQL database errors 

    # Connect to the WhatABook database
    db = mysql.connector.connect(**config)  

    cursor = db.cursor() 

    print("\n  Welcome to the WhatABook Application! \n\n  Please select a chapter.")

    # When any other option besides "4"
    user_selection = show_menu() 
    while user_selection != 4:

        # Option 1 shows all Books, Option 2 shows locations, Option 3 selects User menu
        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                # Option 1 shoes the current wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # Option 2 goes to the list of books to add to wishlist
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)

                    # User input to Select the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                if book_id <1 or book_id > 9:
                    print('\n        But that Book ID is not in our library! Please try another. Sorry!')  
                    sys.exit()
                # If the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")
                
                # Show the account menu 
                account_option = show_account_menu()

        # If the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # Show the main menu
        user_selection = show_menu()

    print("\n  Thanks for choosing WhatABook! \n")

except mysql.connector.Error as err:

    # MySQL database error messages
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    
    # Close the connection to MySQL
    db.close()
