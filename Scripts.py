from QuickSort import quickSort
from ShellSort import startShellSort

list = [16, 9, 15, 90, 4]
# list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
numbersList = list.copy()
numbersList2 = list.copy()

h1 = 2
h2 = 5


startShellSort(numbersList, h1, h2)

quickSort(numbersList2, 0, len(numbersList2)-1)

print(numbersList2)
