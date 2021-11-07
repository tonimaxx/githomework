# Algorithm Homework 3

# 1. Below the Arithmetical Mean
# [1,3,4,5,6,10,2,3] > [1,3,4,2,3]

def below_mean(numarray):
    new_list = []
    mean = sum(numarray)/len(numarray)
    for i in numarray:
        if i < mean:
            new_list.append(i)
    return new_list

print(below_mean([1,3,4,5,6,10,2,3])) # [1, 3, 4, 2, 3]
print(below_mean([1,3,4,5,6,10,2,3,20,15,17])) #[1, 3, 4, 5, 6, 2, 3]


# 2. Two Lowest Elements
# [198,3,4,9,10,9,2] > [2,3]
# Avoid internal function numbers.sort()

def two_lowest(numarray):
    new_list = []
    for i in range(0, len(numarray)):
        for n in range(i + 1, len(numarray)):
            if (numarray[i] > numarray[n]):
                z = numarray[i]
                numarray[i] = numarray[n]
                numarray[n] = z
    a = 0
    i = 0
    while a < 2:
        if a == 0:
            new_list.append(numarray[i])
            i += 1
            a += 1
        else:
            if numarray[i] != numarray[i - 1]:
                new_list.append(numarray[i])
                i += 1
                a += 1
            else:
                i += 1
    return new_list

print(two_lowest([198,3,4,9,10,9,2])) # [2, 3]
print(two_lowest([198,3,4,9,2,10,9,2,2,2,3] )) # [2, 3]
print(two_lowest([198,1,1,3,4,9,2,10,9,2,2,2,3,1] )) # [1, 2]