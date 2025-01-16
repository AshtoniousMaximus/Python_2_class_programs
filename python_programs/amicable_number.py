# answer for amicable number program, euler 21
# written on 11/14/2024
# created by Ashton Pankey


# this is called d(n) in the problem
def sum_div(n):
    sums = 0
    divisors = []
    for i in range(1,n):
        if n % i == 0 and i !=n :
            divisors.append(i)
            sums+= i
    return sums

# print(divisors)
# print(sums)

# print(sum_div(220))

# print(sum_div(sum_div(12)))

# this is called d(d(n)) in the problem
def amicables(n):
    sum = 0
    amicable_numbers = []
    for i in range(1,n):
        # if number is equal to d(d(i)) and i si not equal to d(i), (for instance 6 and 28 are not amicable)
        if i == sum_div(sum_div(i)) and i != sum_div(i) :
            amicable_numbers.append(i)
            sum += i
    return print(amicable_numbers, sum)

amicables(10000)
# 220 + d(220) = 220 +284 = 504
# 284 + d(284) = 284 + 220 = 504
# for i in range(1,100):
#     print(f"i = {i} --> d(i) ")
# print(f"the number {n} has divisors {divisors} which adds together into {sums}")