def shellSortAlgorithm(numList, h):
    while h > 0:

        for startPosition in range(h):
            shellShiftingElements(numList, startPosition, h)

        h = h // 2


def shellShiftingElements(numList, startPosition, h):
    for pos in range(startPosition + h, len(numList), h):

        currentValue = numList[pos]
        currentPosition = pos

        while currentPosition >= h and numList[currentPosition - h] > currentValue:
            numList[currentPosition] = numList[currentPosition - h]
            currentPosition = currentPosition - h

        numList[currentPosition] = currentValue


def startShellSort(numList, h1, h2):
    originalList = numList.copy()
    print("Shell sort")
    shellSortAlgorithm(originalList, h1)
    print("Shell sort result for h =", h1, " : ", originalList)
    shellSortAlgorithm(numList, h2)
    print("Shell sort result for h =", h2, " : ", numList)
