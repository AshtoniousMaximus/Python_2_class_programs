# Decorators
# created by Ashton Pankey
# last Revised: 10/15/2024

# fact 1: you can alias a function



def alias_example():
    print('this is the alias_example function')

a_ex = alias_example
# a_ex()

# fact 2: you can define a function within a function
# fact 3: you can return a function from within a function

def outer_function():
    def inner_function():
        print('this is the inner function')
    print('this is the outer function')
    return inner_function()
# outer_function()


# this is useful because of wrappers: making an existing function different
def custom_greeting(word):
    def greeting():
        print(f"{word}, it's great to have you")

    return greeting

german_greeting = custom_greeting("Wilkommen")
french_greeting = custom_greeting("Bienvenue")

german_greeting()
french_greeting()




# this is a function wrapper, it wrapps functions, basically 'translating' the function into another functon
def wrapping_function(function_to_be_wrapped):
    def wrapped_function():
        function_to_be_wrapped()
        print("running a function")
    return wrapped_function

# both parts work the same, wrapping_function(french_greeting) only gives the function itself, it is not telling it to run

wrapping_function(french_greeting)()

# this is better because this stores the translated function rather than continuously translating the function every time it is called
new_french_greeting = wrapping_function(french_greeting)
new_french_greeting()

# doesn't have to be called something else, this re aliases the old function 
french_greeting = wrapping_function(french_greeting)
french_greeting()


# just take this function and wrap it with wrapping function
@wrapping_function
def decorator_example():
    print('this is decorated')

decorator_example()

# decorator is a function that calls another function and wraps it. good for debugging