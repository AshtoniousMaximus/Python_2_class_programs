# collatz conjecture challenge
# created by Ashton Pankey
# revised on 12/03/2024

def collatz_function(number: int, counter: int):
    if number == 1:
        # counter += 1
        return counter
    elif number % 2 == 0:
        number = number/2
        # counter += 1
    else:
        number = 3*number + 1
        # counter += 1
    return collatz_function(number, counter+1)


longest_so_far_number = 0
longest_so_far_length = 0

for i in range(1, 1000):

    length = collatz_function(i, 1)
    if length > longest_so_far_length:
        longest_so_far_length = length
        longest_so_far_number = i
    collatz_function(i, 1)

print(f"the longest collatz number is {longest_so_far_number} with a length of {longest_so_far_length}")
