import numpy as np

A = np.random.randint(1, 10, (3, 5))
B = np.random.randint(1, 10, (5, 2))

print(np.dot(A, B))

v = np.array([1, 2, 3])
M = np.random.randint(1, 10, (5, 3))

print(np.dot(M, v))

C = np.random.randint(1, 10, (3, 3))
b = np.array([1, 2, 3])

print(np.linalg.solve(C, b))
print(np.linalg.det(C))
print(np.linalg.inv(C))
print(C.T)