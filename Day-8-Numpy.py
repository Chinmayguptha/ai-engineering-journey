a = [ 1 , 2 , 3 ]

b = [ 4 , 5 , 6 ]

print(a+b)

res = []

for i in range(len(a)):
    res.append(a[i] + b[i])

print(res)



import numpy as np

a = np.array([1,2,3,4,5])

b = np.array([6,7,8,9,10])

print(a+b)


c = np.array([1,2,3])
print(c)

d = np.array(["hello" , "haii" , "hmt"])
print(d)

print(type(d))

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.shape)

a1 = np.array([['P' , 'C' , 'D'] , ['l','n' , 'm']])
print(a1.shape)


print(a.ndim)


mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[0])

print(mat[1][2])

print(mat[0:2])

print(mat[1:2])


print(np.zeros( (2,4 )))

print(np.ones((2,2)))

print(np.arange(0,10,2))

print(np.eye(2))


arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr[1][0])


print(np.linspace(0, 1, 5))

arr = np.array([1,2,3,4,5,6])

new_arr = arr.reshape(2,3)

print(new_arr)


print(arr.shape)

print(arr.size)

print(arr.dtype)

print(arr.ndim)