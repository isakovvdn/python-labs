import re

text = input("Введите текст: ")

words = re.findall(r"\b[A-Z][A-Za-z]*\d{2}(\d{2})?\b", text)
result = re.finditer(r"\b[A-Z][A-Za-z]*\d{2}(\d{2})?\b", text)

for match in result:
    print(match.group())