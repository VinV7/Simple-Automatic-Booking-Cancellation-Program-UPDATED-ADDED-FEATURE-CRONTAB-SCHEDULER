import psycopg2
from psycopg2 import extras
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") #Your YCBM API KEY here
ACCOUNT_ID = os.getenv("ACCOUNT_ID") #Your YCBM Account ID here
EMAIL = os.getenv("EMAIL") #The Email you used for the YCBM API here
TIME_GIVEN = 900 #The amount of time given to pay (1 minute = 60 seconds, 900 seconds = 15 minutes)

def connect_to_postgresql(): #Function to connect to the database
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USERNAME"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST_SERVER"),
            port=os.getenv("PORT"),
        )
        print("Connected to PostgreSQL")
        return connection
    except psycopg2.OperationalError as errors:
        print("Unable to connect to the database : ", errors)
        return None

def cancel_unpaid_bookings():
        connection = connect_to_postgresql()
        if connection is None:
            return 
            
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            #GET every single data inside of the Database
            read_table_script = "SELECT * FROM orders_book INNER JOIN transactions ON (orders_book.book_code = transactions.book_code)"
            cursor.execute(read_table_script)

            for record in cursor.fetchall():
                #Check if there's a table with the book_status = 'booked' and the payment status = 'unpaid'
                if record['book_status'] == "booked" and record['payment_status'] == "unpaid":
                    booking_time = record['created_at']
                    current_time = datetime.now()
                    time_difference = current_time - booking_time

                    #Check if it's been 15 minutes since booking and payment is still unpaid
                    if time_difference.total_seconds() >= TIME_GIVEN: 
                        cancel_book_order = "UPDATE orders_book SET book_status = 'cancelled' WHERE book_status = 'booked'"
                        cursor.execute(cancel_book_order)
                        print("Cancellation Successful!")
                        connection.commit()
                        connection.close

def update_the_YCBM_sessions():
    connection = connect_to_postgresql()
    if connection is None:
        return
    try:    
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            #Function to get the book_id/code from the table with the book_status == "cancelled"
            read_table_script = "SELECT * FROM orders_book INNER JOIN transactions ON (orders_book.book_code = transactions.book_code)"
            cursor.execute(read_table_script)

            #Function to cancel the book session and update the website
            for record in cursor.fetchall():
                if record['book_status'] == 'cancelled':
                    book_id = record['book_id']
                    update_booking_session_url = f"https://api.youcanbook.me/v1/bookings/{book_id}"
                    
                    headers = {
                        "Content-Type": "application/json",
                    }
                    
                    payload = {
                        "cancelled": True,
                    }
                    
                    response = requests.patch(update_booking_session_url, headers=headers, json=payload, auth=(EMAIL, API_KEY)) 
                    if response.status_code == 200:
                        print('Booking Cancellation Succesful')
                    else:
                        print('Failed to Cancel the booking session. Error:\n', response.text)

    #Close / Shutdown connection to the Database
    finally:
        connection.close()

cancel_unpaid_bookings()
update_the_YCBM_sessions()