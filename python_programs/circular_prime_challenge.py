# circular prime number challenge


from sympy import isprime
# test_number = 197
test_number = 1000000

def circularizer(number):
    to_circularize = str(number)
    rotations = []
    for i in range(len(to_circularize)):
        rotations.append(int(to_circularize))
        to_circularize = to_circularize[1:]+to_circularize[0]
        # print(to_circularize)
    return rotations

# print(isprime(197))

def is_circular_prime(number):
    """Returns true or false"""

    # potentially faster
    if isprime(number):
        rotations = circularizer(number)
        for rotation in rotations:
            if not isprime(rotation):
                return False
        return True

    #  # uses slick list comprehension
    #     isprimes = [isprime(rotation) for rotation in rotations]
    #     if False in isprimes:
    #         return False
    #     else: return True
    # else:
    #     return False



# def get_circular_primes(limit = int):
#     for i in range(limit+1):

circular_primes = []
for i in range(test_number):
    if is_circular_prime(i):
        circular_primes.append(i)
        print(i)
print(f"there are {len(circular_primes)} circular primes in {test_number}")
print(circular_primes)