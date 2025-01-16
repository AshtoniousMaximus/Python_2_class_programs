# Sieve of Eratosthenes program
# created by Ashton Pankey
# revised on 11/7/2024

# creating the sieve with for loops

def sieve(stop_value):
    # this is list comprehension "which is fucking killer!" or "fucking sick!"
    # it tells you what to do with an old list
    values = [True for i in range(stop_value+1)]
    values[0] = False
    values[1] = False

    primes = []

    for i in range(len(values)):
        if values[i]:
            number_of_iterates = int(stop_value/i)
            for j in range(2, number_of_iterates+1):
                values[i*j] = False
    for i in range(len(values)):
        if (values[i] == True):
            primes.append(i)
    return print(f"primes: {primes}")


# print(sieve(100))


# creating a sieve with dictionaries

def sieve2(stop_value):
    """ returns a dictionary of numbers and True/False indicating prime status"""
    ''' other methods to populate the numbers list
    # # classic 
    # numbers = []
    # for i in range(stop_value+1):
    #     numbers.append(i)

    # # carmine special
    # numbers = list(range(stop_value + 1)) '''

    # use list comprehension to populate a list of numbers and a list of True
    numbers = [i for i in range(stop_value+1)]
    values = [True for i in range(stop_value+1)]

    # 0 and 1 are not prime by definition
    values[0] = False
    values[1] = False
    
    # zip the two list together and make it a dictionary
    prime_table = dict(zip(numbers,values))

    # running the sieve of Eratosthenes
    # go through the dictionary
    for number, is_prime in prime_table.items():

        # if we run into a number with true, that number is prime, we set all multiples of it to false
        if is_prime == True:
            # calculate how many multiples there are
            number_of_iterates = stop_value//number
            # updates all multiples to a value of false
            for j in range(2, number_of_iterates + 1):
                prime_table[number*j] = False
    # prime table now contains correctly flagged numbers
    return prime_table

if __name__ == "__main__":
    primes = sieve2(10)
    print([number for number, value in primes.items() if value])