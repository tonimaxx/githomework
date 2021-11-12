# Algorithm Homework 4

# 1. Even First
# [7,3,5,6,4,10,3,2] > [6,4,10,2,7,3,5,3]
# Solve with without allocating additional storage, operate with the input array

def even_first(numarray):
    i = 0
    count = len(numarray)
    while i < count:
        if numarray[i] % 2 == 0:
            numarray.append(numarray[i])
        i += 1
    i = 0
    while i < count:
        if numarray[i] % 2 != 0:
            numarray.append(numarray[i])
        i += 1
    return numarray[count:]

print(even_first([7,3,5,6,4,10,3,2])) # [6, 4, 10, 2, 7, 3, 5, 3]
print(even_first([1,5,2,3,8,4,11,182])) # [2, 8, 4, 182, 1, 5, 3, 11]

# 2. Increment a Number
# [1,2,9] > [2,3,0]

def increment_number(numarray):
    temp = []
    for i in numarray:
        lastdigit = int(repr(i)[-1]) # Take the last digit of input more than one digit
        temp.append(int(repr(lastdigit+1)[-1])) # In case 9+1, take the last digit (0) as well.
    return temp

print(increment_number([1,2,9])) # [2, 3, 0]
print(increment_number([10,21,32])) # [1, 2, 3]
print(increment_number([555,176,899])) # [6, 7, 0]


