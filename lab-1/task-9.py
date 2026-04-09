money = {
    5000: 2,
    1000: 10,
    500: 5,
    100: 20,
    50: 10,
    10: 30
}

amount = int(input())
rest = amount
result = []

for nominal in sorted(money.keys(), reverse=True):
    count = min(rest // nominal, money[nominal])
    if count > 0:
        result.append(f"{count}*{nominal}")
        rest -= count * nominal

if rest != 0:
    print("Операция не может быть выполнена!")
else:
    print(" + ".join(result))