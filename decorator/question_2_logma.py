# Write a logme decorator that logs the function call by writing to the log the function name
# and its parameters. After that, it should call the function, and then log that the function
# has finished with the function name.

# Add this decorator to the following function and then run it:

#-------------------------------------------------------------------------------------------

import time
import logging

logging.basicConfig(filename='apps.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Logme decorator
def logme(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

# Time measuring decorator
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute")
        return result
    return wrapper

# Applying both decorators
@logme
@time_decorator
def star_print(msg):
    print('************', msg)

# Running the function
star_print("Hello, logme decorator 😄")
