"""
create the funcion BubbleSort
Define the values of ints to be sorted with bubble sort
define the length of the values (n)
iter over values elements:
    iter over positions(n-j-1)
    if the element of values is > than the element(n+1)
    swap position
    define as doneSwap

"""

values = [1, 3, 6, 2, 6, 7, 3, 22, 48, 12312, 23, 24 , 999999999]


def bubblesort(values):
    n = len(values)
    for i in range(n):
        doneSwap = False
        for j in range(0, n - 1 - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                doneSwap = True
        if not doneSwap:
            break


bubblesort(values)
print("The values will br sorted as " + str(values))

