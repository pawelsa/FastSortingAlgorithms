import random


def partitioning_pivotChoosing(arr, left, right):
    pivotValue = arr[right]
    leftIndex = left - 1

    for j in range(left, right):  # ew     right - 1
        if arr[j] <= pivotValue:
            leftIndex = leftIndex + 1
            arr[leftIndex], arr[j] = arr[j], arr[leftIndex]

    arr[leftIndex + 1], arr[right] = arr[right], arr[leftIndex + 1]
    return leftIndex + 1


def medianOfThree_pivotChoosing(arr, left, right):
    mid = int((left + right) / 2)
    if arr[right] < arr[left]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] < arr[left]:
        arr[mid], arr[left] = arr[left], arr[mid]
    if arr[right] < arr[mid]:
        arr[right], arr[mid] = arr[mid], arr[right]
    return mid


def randomized_pivotChoosing(arr, left, right):
    randomNumber = random.randint(left, right)
    arr[right], arr[randomNumber] = arr[randomNumber], arr[right]
    return partitioning_pivotChoosing(arr, left, right)


def first(arr, left, right):
    arr[0], arr[right] = arr[right], arr[0]
    return partitioning_pivotChoosing(arr, left, right)


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place

        # pi = medianOfThree_pivotChoosing(arr, low, high)
        # pi = randomized_pivotChoosing(arr, low, high)
        # pi = partitioning_pivotChoosing(arr, low, high)
        pi = first(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
