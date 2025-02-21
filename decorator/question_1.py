# Write a password decorator that asks the user to enter a password.
# If the user enters the correct password (for this exercise, the password will be "1234"),
# the function will be executed. If not, a message "password wrong" will appear,
# and the function will not be executed.

# Additionally, log a message for each failed password attempt.

# Apply the decorator to the following function and then execute it:

#------------------------------------------------------------------------------------------

import logging

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Password decorator
def password(func):
    def wrapper(*args, **kwargs):
        user_input = input("Enter password: ")
        if user_input == "1234":
            return func(*args, **kwargs)
        else:
            print("password wrong")
            logging.warning(f"Failed password attempt for function [{func.__name__}]")
    return wrapper

# Applying the decorator
@password
def say_hello():
    print('hello...')

# Call the function
say_hello()
