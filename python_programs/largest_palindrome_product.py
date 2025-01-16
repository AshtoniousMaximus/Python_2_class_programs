# Euler problem 4
# created by Ashton Pankey
# revised 11/21/2024

def reverse_number(number):
    number_string = str(number)

# good conceptually
    # new_number_string = ''
    # for i in range(len(number_string)):
    #     new_number_string += number_string[len(number_string)-1-i]
    # return int(new_number_string)

# more efficient
    return int(number_string[::-1])
    
# print(reverse_number(123456))



def check_palindrome(number):
    if number == reverse_number(number):
        return True
    else:
        return False
    
print(check_palindrome(12345654321))

def biggest_palindrome(number):
    biggest_so_far = (0,0,0)
    for i in range(number):
        for j in range(number):
            product = i*j
            if check_palindrome(product):
                if product > biggest_so_far[2]:
                    biggest_so_far = (i,j,product)
    return biggest_so_far

print(biggest_palindrome(100000))