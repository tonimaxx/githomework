# Compute the sum of digits in all numbers from 1 to n.
def sum_n(n):
    i = 0
    while n > 0:
        i += n
        n -= 1
    return i

print(sum_n(5))

# Find Max Number
max_number = 0
n = 0
while n < 3:
    x = int(input())
    max_number = x if x > max_number else max_number
    n += 1
print(f"Max Number is {max_number}")

# Count odd and even numbers
def count_odd_even(number):
    odd = 0
    list = [*str(number)]
    for i in list:
        odd = odd+1 if (int(i) % 2) == 0 else odd
    return (len(list)-odd), odd

number = 11112222
odd, even = count_odd_even(number)
print(f"{number} consists of {odd} odd(s) and {even} even(s) numbers.")




