import re

filename = input("Введите имя файла: ")
variant = int(input("Введите номер варианта: "))

patterns = {
    1: r"\b\d{2}-\d{2}-\d{4}\b",
    2: r"\b\d{2}:\d{2}:\d{2}\b",
    3: r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    4: r"\b(?:int|short|byte)\s+\w+\s*=\s*\d+\b",
    5: r"\(\d{3}\)\d{7}|\(\d{3}\)\d{3}-\d{2}-\d{2}",
    6: r"\b\w+\s*:\s*(?:int|short|byte)\s*\[\d+\]\b",
    7: r"(:-?\)+)",
    8: r"\b\w+\s*&{1,2}\s*\w+\b",
    9: r"\b83\d{3},\s*Донецк\b",
    10: r"[A-Za-z]:\\(?:[\w.-]+\\?)+"
}

pattern = patterns[variant]

with open(filename, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        for match in re.finditer(pattern, line):
            print(f"Строка {line_number}, позиция {match.start() + 1} : найдено '{match.group()}'")