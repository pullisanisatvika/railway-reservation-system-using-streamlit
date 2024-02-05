# railway-reservation-system

Features of the Railway Reservation System Using Streamlit Project
-Railway Reservation have user registration and login.
-Train Search and Availability.
-Add Trains and delete trains
-Cancel Tickets 
-Booking and cancelling tickets.

Software Requirement to run this project
-You Need To Install Pycharm IDE or VSCODE 
-You Need To have Github Account To host application
-You Need To have Python 3.9 or above version
Tools and Technologies to be used in this project

-Use VSCODE To Run Application.
-Create Account In Github and Streamlit Account.
-Database is SQLITE (no need to install software)

How To Import And Run The Project?
-First Install VSCODE OR PYCHARM
-EXTRACT ALL THE FILES INSIDE THE RAR.
-DATABASE AND MAIN.PY INSIDE THE RAR AND OPEN THE VSCODE
-RUN PROJECT IN TERMINAL
-TYPE THE CODE(streamlit run main.py)
-Local host will be generated for output.
-IF YOU WANT HOST USE STREAMLIT WEBSITE.

How To Import Database?
-DATABASE WILL BE SQLITE.
-NO NEED TO INSTALL ANY SOFTWARE.
-EXTRACT AND RUN.


A small jist of whats happening around
Database:

SQLite3:
A lightweight, file-based database used to store and manage railway data.
Tables:
trains: Stores train information (number, name, departure date, destinations).
seats_<train_number>: Created for each train to manage seat details (number, type, booking status, passenger info).
users: Likely intended for storing user login credentials (not fully implemented in the provided code).
employees: Intended for employee records (designation, etc., not fully implemented).
Software:

Python: The primary programming language used to write the code.
Streamlit: A Python library for building interactive web applications. It creates the user interface for the railway system.
Pandas: A Python library for data analysis and manipulation. It's used to create and display dataframes in the application.
Code Structure and Functionality:

Import necessary libraries:

import streamlit as st
import sqlite3
import pandas as pd
Database connection:

conn = sqlite3.connect('railway_system.db')
c = conn.cursor()
Functions for database operations:

create_DB_if_Not_available(): Creates tables if they don't exist.
add_train(): Adds a new train to the database.
delete_train(): Deletes a train and its corresponding seat table.
create_seat_table(): Creates a seat table for a train.
categorize_seat(): Categorizes a seat as Window, Aisle, or Middle.
allocate_next_available_seat(): Finds the next available seat of a specified type.
book_ticket(): Books a ticket by updating seat details and passenger information.
cancel_tickets(): Cancels a ticket by marking the seat as unbooked.
search_train_by_train_number(): Searches for a train by its number.
search_trains_by_destinations(): Searches for trains based on starting and ending destinations.
view_seats(): Displays seat availability for a train.
Train functions (using Streamlit):

train_functions(): Main function that handles user interactions and calls database functions to perform actions like:
Adding a new train
Viewing all trains
Searching for trains
Deleting a train
Booking a ticket
Canceling a ticket
Viewing seat availability
Closing the database connection:

conn.close()
