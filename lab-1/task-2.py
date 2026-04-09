numbers = [1, 2, 3, 5, 8, 13]

result = True

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        result = False
        break

print(result)