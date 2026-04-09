import random

n = random.randint(1, 10000)
arr = [random.randint(0, 100) for _ in range(n)]

size = 1
while size < n:
    size *= 2

arr += [0] * (size - n)

print("n =", n)
print("Итоговый размер =", len(arr))
print(arr)