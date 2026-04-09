s = input()

try:
    s = s.replace(',', '.')
    value = float(s)

    if value < 0:
        raise ValueError

    rub = int(value)
    kop = round((value - rub) * 100)

    if kop == 100:
        rub += 1
        kop = 0

    print(f"{rub} руб. {kop:02d} коп.")
except:
    print("Некорректный формат!")