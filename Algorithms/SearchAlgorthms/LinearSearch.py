""" Linear Search is a sequential searching algorithm where we start from one end and check every element of the list until the desired elemt is found..kit is the simplest alogorithm
"""

# Linear Search in Python


def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [4500, 76, 80, 61, 19]
x = 80
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
