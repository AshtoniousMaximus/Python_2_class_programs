# Additional decorators
# created by Ashton Pankey
# Revised on 10/15/2024

from utilities import path

def run_counter(f):
    def ran(*args,**kwargs):
        ran.calls += 1
        return f(*args,**kwargs)
    ran.calls = 0
    return ran


        
@run_counter
def for_loop_factorial(n):
    result = 1
    for i in range(n):
        result = result*(i+1)
    print(f'the factorial of {n} is {result}')
    return result


while True:
    x = input('enter an integer to find the factorial\n')
    # for_loop_factorial.calls = 0
    try:
        for_loop_factorial(int(x))
        print(f'this function was called {for_loop_factorial.calls} times')
    except:
        print('invalid input')
