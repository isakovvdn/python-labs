from collections import Counter

filename = input("Введите имя файла: ")

with open(filename, "r", encoding="utf-8") as file:
    text = file.read().lower()

letters = [ch for ch in text if ch.isalpha()]
counter = Counter(letters)

for ch, count in counter.most_common():
    print(ch, count)