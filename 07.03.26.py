class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value
for x in EvenIterator(10):
    print(x)

data = [10, 20, 30]
class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value
for x in ReverseList(data):
    print(x)


import numpy as np
arr1 =([3, 7, 1, 9, 4])
mx = np.max(arr1)
mn = np.mean(arr1)
print("среднее значение:", mn, "Максимальный:", mx)

arr2 = np.array([2, 8, 4 ,10, 3])
res = arr2[arr2 > 5]
print(res)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a+b
print(c)

arr3 = np.array([1, 2, 3, 4])
arr3x3 = arr3*3
print(arr3x3)