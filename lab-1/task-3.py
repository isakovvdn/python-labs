card = input().replace(' ', '')

if len(card) == 16 and card.isdigit():
    print(card[:4], "****", "****", card[-4:])
else:
    print("Некорректный номер")