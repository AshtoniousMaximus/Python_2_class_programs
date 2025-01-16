from time import time

def timer(function_to_be_wrapped):
    def wrapped_function(*args,**kwargs):
        start_time = time()
        print(f"running a function at {start_time}")
        function_to_be_wrapped(*args,**kwargs)
        end_time = time()
        print(f'function stopped at {end_time}')
        run_time  = end_time-start_time
        print(f'time elapsed: {round(run_time,3)} seconds')
    return wrapped_function

@timer
def testing(n,power = 5):
    for i in range(n):
        i**power

# testing(100000000,power = 7)

# examples 4*3*2*1
@timer
def for_loop_factorial(n):
    result = 1
    for i in range(n):
      result = result*(i+1)
    print(result)
    return result


# for_loop_factorial(10000)
@timer
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
# recursive_factorial(10)

# human FActor tree
# 420 = 42*10 = 7*6 * 2*5 =7*2*3*2*5 =2^2 *3 * 5 * 7


# computer FActor tree should spit out that result and take any number
# factor(420) = 2*factor(210) = 2 * 2 * factor(105) = 2*2*3*factor(35) = 2*2*3*5factor(7) = 2*2*3*5*7