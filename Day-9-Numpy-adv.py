import numpy as np

arr = np.array([1, 4, 9])

print(np.sqrt(arr))

print(np.sin(arr))

print(np.exp(arr))

print(np.abs(arr))


print(arr.dtype)


a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a, b))


a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(a @ b)


nums = [1,2,3,4,5]

mean = sum(nums) / len(nums)

print(mean)

nums = [1,2,3,4,5]

mean = sum(nums)/len(nums)

variance = sum((x - mean)**2 for x in nums)/len(nums)

print(variance)

A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

result = [
    [0,0],
    [0,0]
]

for i in range(2):

    for j in range(2):

        for k in range(2):

            result[i][j] += A[i][k] * B[k][j]

print(result)