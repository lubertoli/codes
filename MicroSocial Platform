# This script implements a simple Twitter-like application using a SQLite database for data storage.
# It supports user registration, login, composing tweets, searching for tweets or users, following users, and displaying a user's main feed.
# The application uses a command-line interface for interaction with the user.

import sqlite3
import getpass
from datetime import date
from os import system, name
import time
import sys 

def clear():
    '''
    Clears the console screen to maintain a clean interface for the user.
    It checks the operating system to execute the appropriate command.
    '''
    if name == 'nt':  # Check if the operating system is Windows
        _ = system('cls')
    else:  # Assume the operating system is Unix/Linux
        _ = system('clear')

def user_login():
    '''
    Handles user login or registration. Users can choose to log in to an existing account or create a new one.
    It establishes a connection to the SQLite database, handles user input, and authenticates or registers the user.
    Returns the user ID of the logged-in user or newly registered user.
    '''
    clear()
    conn = sqlite3.connect('./twitter.db')
    cursor = conn.cursor()

    # Loop until a valid choice is made
    while True:
        try:
            userinput = int(input("If you want to login into an existing account enter '1'. \nIf you want to create a new account enter '2'. \nEnter choice: "))
            if userinput not in [1, 2]:
                raise ValueError("Invalid input")
            break
        except ValueError as e:
            print(f"{e}. Please enter '1' or '2'.")

    if userinput == 1:  # User chose to log in
        return login_existing_user(cursor)
    elif userinput == 2:  # User chose to register a new account
        return register_new_user(cursor, conn)

def login_existing_user(cursor):
    '''
    Handles the login process for an existing user.
    Prompts the user for their user ID and password, and authenticates them against the database.
    Returns the user ID of the authenticated user or None if authentication fails.
    '''
    clear()
    print("LOGIN")
    while True:
        login_id = input("Enter userID: ")
        password = getpass.getpass("Enter password: ")
        cursor.execute("SELECT * FROM users WHERE usr=? AND pwd=?", (login_id, password))
        account = cursor.fetchone()
        if account:
            clear()
            print("Logging in...")
            time.sleep(2)
            return login_id
        else:
            print("\nIncorrect user ID or password. Please try again.")

def register_new_user(cursor, conn):
    '''
    Handles the registration of a new user.
    Prompts the user for their desired user ID, name, email, city, timezone, and password.
    Checks if the user ID is already taken and, if not, inserts the new user into the database.
    Returns the user ID of the newly registered user.
    '''
    clear()
    print("REGISTER NEW ACCOUNT")
    while True:
        newloginid = input("Enter a new user ID: ")
        cursor.execute("SELECT usr FROM users WHERE usr = ?", (newloginid,))
        if cursor.fetchone():
            print("This user ID has already been registered. Please try again with a different user ID.")
        else:
            break

    newusername = input("Please enter your name: ")
    newuseremail = input("Please enter your email: ")
    newusercity = input("Please enter your city: ")
    newusertimezone = input("Please enter your timezone: ")
    password = getpass.getpass("Please enter your password: ")
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", (newloginid, password, newusername, newuseremail, newusercity, newusertimezone))
    conn.commit()
    print("\nRegistration successful.")
    time.sleep(2)
    return newloginid

