# factor tree
# created by Ashton Pankey
# revised 10/19/2024

# creates a factor tree function that takes a variable n
def recursive_factor_tree(n):
    # creates numbers that count how many times n was divisible by that number
    twos = 0
    threes = 0
    fives = 0
    sevens = 0
    # creates a variable that is equal to n before anything is done to it
    initial = n
    # runs a while loop that recursively breaks down the number
    while True:
        # if the number is divisible by 2, it divides it by 2 and adds 1 to twos
        if n%2 == 0:
            n =  n/2
            twos +=1
        # if the number is divisible by 3, it divides it by 3 and adds 1 to threes
        elif n%3 == 0:
            n =  n/3
            threes += 1
        # if the number is divisible by 5, it divides it by 5 and adds 1 to fives
        elif n%5 == 0:
            n =  n/5
            fives += 1
        # if the number is divisible by 7, it divides it by 7 and adds 1 to sevens
        elif n%7 == 0:
            n = n/7
            sevens += 1
        # otherwise, n isn't changed and the loop is broken
        else:
            n = n
            break
    # if 2 was divided 0 times, two_print becomes an empty string
    if twos == 0:
        two_print = ''
    # otherwise it prints to what power 2 was divided by
    else: 
        two_print = f'2^{twos}*'

    # if 3 was divided 0 times, three_print becomes an empty string
    if threes == 0:
        three_print = ''
    # otherwise it prints to what power 3 was divided by
    else: 
        three_print = f'3^{threes}*'

    # if 5 was divided 0 times, five_print becomes an empty string
    if fives == 0:
        five_print = ''
    # otherwise it prints to what power 5 was divided by
    else: 
        five_print = f'5^{fives}*'

    # if 7 was divided 0 times, seven_print becomes an empty string
    if sevens == 0:
        seven_print = ''
    # otherwise it prints to what power 7 was divided by
    else: 
        seven_print = f'7^{sevens}*'
    # returns a print line that tells the user the initial value of n and an exponentail notation factor tree
    return print(f'the factor tree of {initial} is {two_print}{three_print}{five_print}{seven_print}{int(n)}')

# creates a user input for creating factor trees
while True:
    # creates an input with instructions
    x = input('enter an integer to find its factor tree\n')
    # creates a try except function to block errors
    try:
        # finds the factorial of the user input by running the function
        recursive_factor_tree(int(x))
    # catches the errors and prints what they were
    except Exception as e:
        print(e)
    
