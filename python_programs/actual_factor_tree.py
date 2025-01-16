# real factor trees
# created by Ashton Pankey
# revised on 10/29/2024



def recursive_factor_tree(n, factors=[]):
    a = int(n)
    for i in range(2,a+1):
        if a%i == 0:
            factors.append(i)
            return recursive_factor_tree(a/i, factors)

    return factors








while True:
    # factors.clear()
    # creates an input with instructions
    x = input('enter an integer to find its factor tree\n')
    # creates a try except function to block errors
    try:
        # finds the factorial of the user input by running the function
        print(recursive_factor_tree(int(x), []))
    # catches the errors and prints what they were
    except Exception as e:
        print(e)
