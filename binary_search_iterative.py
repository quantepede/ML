"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""

    # case when array contains even no of elements
    if len(input_array) % 2 == 0:
        dropped = 0

        while len(input_array) > 1:
            midindex = int(len(input_array) / 2 - 1)
            # case when input array has even elements
            if value == input_array[midindex]:
                print("value found 1")
                return dropped+midindex

            elif value > input_array[midindex]:
                print("elif")
                dropped += len(input_array[:midindex+1])
                input_array = input_array[midindex+1:]
                print(input_array)
            else:
                print("else")
                input_array = input_array[:midindex]
                print(input_array)

        if value == input_array[0]:
            print("value found 2")
            return dropped

        else:
            print("value not found")
            return -1

    # case when array contains odd no of elements
    else:
        dropped = 0

        while len(input_array) > 1:
            midindex = int(len(input_array) // 2)
            # case when input array has even elements
            if value == input_array[midindex]:
                print("value found 1")
                return dropped + midindex

            elif value > input_array[midindex]:
                print("elif")
                dropped += len(input_array[:midindex + 1])
                input_array = input_array[midindex + 1:]
                print(input_array)
            else:
                print("else")
                input_array = input_array[:midindex]
                print(input_array)

        if value == input_array[0]:
            print("value found ")
            return dropped

        else:
            print("value not found")
            return -1


test_list = [1,3,9,15,19,29,30]
test_val1 = 30
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))