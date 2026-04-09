import os
import hashlib

directory = input("Введите путь к директории: ")
hashes = {}

for root, dirs, files in os.walk(directory):
    for name in files:
        path = os.path.join(root, name)
        with open(path, "rb") as file:
            data = file.read()
            file_hash = hashlib.md5(data).hexdigest()

        if file_hash not in hashes:
            hashes[file_hash] = []
        hashes[file_hash].append(path)

found = False

for group in hashes.values():
    if len(group) > 1:
        found = True
        print("Дубликаты:")
        for item in group:
            print(item)
        print()

if not found:
    print("Дубликаты не найдены")