"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(partition):
    # base case, list has 0 or 1 element, returns without sorting
    if len(partition) <= 1:
        return partition

    else:
        print("err", partition)
        pivot_value = partition[-1]
        pivot_index = len(partition) - 1

        index = 0
        while index < len(partition):

            # stops comparing when current partition is sorted
            if pivot_index <= index:
                if len(partition) == 2:
                    return partition
                else:

                    print("sort lower list:", partition[:pivot_index])

                    print("sort higher list:", partition[pivot_index + 1:])
                    a = quicksort(partition[:pivot_index])

                    b_aslist = []
                    b_aslist.append(partition[pivot_index])


                    print("sort pivot item:", b_aslist)


                    b = quicksort(b_aslist)
                    c = quicksort(partition[pivot_index + 1:])

                    return a+b+c

            print(f"comparing {pivot_value} ({pivot_index}) to {partition[index]} ({index})")
            if (pivot_value < partition[index]):

                print("before:   ", partition)
                copy_pivot = pivot_value

                # overwrite pivot value with compared
                partition[pivot_index] = partition[index]

                # move value before pivot to beginning
                partition[index] = partition[pivot_index-1]

                # move pivot to index before pivot value
                partition[pivot_index-1] = pivot_value

                print("iteration:", partition)

                pivot_index = pivot_index - 1

            # if the value moved is greater than pivot, dont increment index and compare again:
            if partition[index] > pivot_value:
                print(f"attention-> {partition[index]} > {pivot_value}")
                # do not increment index

            else:
                index += 1

        return partition


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# print(quicksort(test))

import random
randomlist = []
for i in range(0,9):
    n = random.randint(-10,10)
    randomlist.append(n)
print("initial random list", randomlist)
print(quicksort(randomlist))