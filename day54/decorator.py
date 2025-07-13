import time
def dely_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@dely_decorator

def say_hello():
   
    print("hello")
@dely_decorator
def say_greeting():
   
    print("how are you?")

def say_bye():
   
    print("Bye")
say_hello()
say_bye()