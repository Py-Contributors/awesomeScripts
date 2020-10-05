# helper methods
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


# algorithms
def bubblesort(A):
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


def insertionsort(A):
    for i in range(1, len(A)):
        key = A[i]

        j = i - 1
        while j >= 0 and key < A[j]:
            swap(A, j, j + 1)
            j -= 1
            yield A


def selectionsort(A):
    for i in range(len(A) - 1):
        pos = i
        for j in range(i + 1, len(A)):
            if A[j] < A[pos]:
                pos = j
        if pos != i:
            swap(A, pos, i)
        yield A


def mergesort(A):
    counter = 1

    while counter < len(A) - 1:
        low = 0

        while low < len(A) - 1:
            mid = low + counter - 1

            high = (2 * counter + low - 1, len(A) - 1)[
                2 * counter + low - 1 > len(A) - 1
            ]

            # merge function is written within mergesort due to limitaion of yield method.
            left, right = A[low : mid + 1], A[mid + 1 : high + 1]

            i, j, k = 0, 0, low
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    A[k] = left[i]
                    i += 1
                elif left[i] > right[j]:
                    A[k] = right[j]
                    j += 1
                k += 1
                yield A

            while i < len(left):
                A[k] = left[i]
                i += 1
                k += 1
                yield A

            while j < len(right):
                A[k] = right[j]
                j += 1
                k += 1
                yield A
            # ending of merge function

            low = low + counter * 2

        counter = 2 * counter


def quicksort(A):
    return


def heapsort(A):
    n = len(A)

    for i in range(n):
        # if child is bigger than parent
        if A[i] > A[(i - 1) // 2]:
            j = i
            # swap child and parent until
            # parent is smaller
            while A[j] > A[(j - 1) // 2]:
                swap(A, j, (j - 1) // 2)

                j = (j - 1) // 2

                yield A
    i = n - 1
    while i >= 0:
        # swap value of first indexed
        # with last indexed
        swap(A, 0, i)

        # maintaining heap property
        # after each swapping
        j, index = 0, 0
        i -= 1
        while True:
            index = 2 * j + 1

            # if left child is smaller than
            # right child point index variable
            # to right child
            if index < (i - 1) and A[index] < A[index + 1]:
                index += 1

            # if parent is smaller than child
            # then swapping parent with child
            # having higher value
            if index < i and A[j] < A[index]:
                swap(A, j, index)

            j = index
            if index >= i:
                break
            yield A
