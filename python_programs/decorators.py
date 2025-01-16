# Additional decorators
# created by Ashton Pankey
# Revised on 10/19/2024

# creates a decorator function that checks how many times a function was run
def run_counter(g):
    # creates the ran function within run_counter that does the counting
    def ran(*args,**kwargs):
        # adds 1 to the calls list
        ran.calls += 1
        # reformats the tuple args to make it more visually appealing
        string_list = [str(element) for element in args]
        # prints a description saying what function ran and the thing it was called upon
        print(f'you are running the function {g.__name__} calling upon: {", ".join(string_list)}')
        # returns the function with arguments and keyword arguments
        return g(*args,**kwargs)
    # sets the calls to zero
    ran.calls = 0
    # returns the ran function
    return ran

# wraps the function for_loop_factorial in the run_counter function 
@run_counter
# creates the for_loop_factorial function with the argument n
def for_loop_factorial(n):
    # creates a float result that has a value of 1
    result = 1
    # creates a for loop that runs through the value of n to find the factorial of n
    for i in range(n):
        # multiplies the number result by 1+result until the final number is reached
        result = result*(i+1)
    # prints what the factorial is
    print(f'the factorial of {n} is {result}')
    # returns the result
    return result

# creates a user interface for the user to enter factorial numbers within a while loop
while True:
    # creates an input with instructions
    x = input('enter an integer to find the factorial\n')
    # creates a try except function to block errors
    try:
        # finds the factorial of the user input by running the function
        for_loop_factorial(int(x))
        # prints how many calls the function has had
        print(f'this function was called {for_loop_factorial.calls} times')
    # catches the errors and prints what they were
    except Exception as e:
        print(e)


