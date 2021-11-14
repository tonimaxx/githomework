# Algorithm Homework 5

# Init Test Environment
test_array = []
test_array.append([15,25,66,7,108,1009,65535,2048])
test_array.append([22,44,33,11,77,66,88,55,99])

print("Test Inputs")
for i in range(0,len(test_array)):
    print(test_array[i])


# 1. Selection Sort
def selection_sort(numarray, is_desc=False):
    for i in range(len(numarray)):
        index = i
        for j in range(i + 1, len(numarray)):
            if is_desc:
                if numarray[index] < numarray[j]:
                    index = j
            else:
                if numarray[index] > numarray[j]:
                    index = j
        numarray[index], numarray[i] = numarray[i], numarray[index]
    return numarray

print('\n#1 Selection Sort')
for test in test_array:
    print(selection_sort(test,True))


# 2. Bubble Sort
def bubble_sort(numarray, is_desc=False):
    is_exchanged = True
    pass_count = 0
    while(is_exchanged):
        is_exchanged = False
        for i in range(len(numarray) - pass_count - 1):
            if is_desc:
                if numarray[i] < numarray[i+1]:
                    numarray[i+1], numarray[i] = numarray[i], numarray[i+1]
                    is_exchanged = True
            else:
                if numarray[i] > numarray[i+1]:
                    numarray[i+1], numarray[i] = numarray[i], numarray[i+1]
                    is_exchanged = True
        pass_count += 1
    return numarray

print('\n#2 Bubble Sort')
for test in test_array:
    print(bubble_sort(test,True))


# 3. Insertion Sort
def insertion_sort(numarray, is_desc=False):
    for i in range(1, len(numarray)):
        index = numarray[i]
        j = i - 1
        if is_desc:
            while j >= 0 and index > numarray[j]:
                numarray[j + 1] = numarray[j]
                j -= 1
            numarray[j + 1] = index
        else:
            while j >= 0 and index < numarray[j]:
                numarray[j + 1] = numarray[j]
                j -= 1
            numarray[j + 1] = index

    return numarray

print('\n#3 Insertion Sort')
for test in test_array:
    print(insertion_sort(test,True))


# 4. Merge Sort
def merge_sort(numarray, isdesc=False):
    return merge_sort_asc(numarray) if not isdesc else merge_sort_desc(numarray)

def merge_sort_asc(numarray):
    if len(numarray) > 1:
        center = int(len(numarray) / 2)
        left = numarray[:center]
        right = numarray[center:]
        merge_sort_asc(left)
        merge_sort_asc(right)
        i = 0
        j = 0
        k = 0 # main pass
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numarray[k] = left[i]
                i += 1
            else:
                numarray[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numarray[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numarray[k] = right[j]
            j += 1
            k += 1
    return numarray

def merge_sort_desc(numarray):
    if len(numarray) > 1:
        center = int(len(numarray) / 2)
        left = numarray[:center]
        right = numarray[center:]
        merge_sort_desc(left)
        merge_sort_desc(right)
        i = 0
        j = 0
        k = 0 # main pass
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                numarray[k] = left[i]
                i += 1
            else:
                numarray[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numarray[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numarray[k] = right[j]
            j += 1
            k += 1
    return numarray

print('\n#4 Merge Sort')
print(merge_sort([88,17,52,65,72,25,65,21,21,28,29,60,48], True))
for test in test_array:
    print(merge_sort(test, True))