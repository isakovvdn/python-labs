import os

music_dir = input("Введите путь к папке с файлами: ")
list_file = input("Введите путь к файлу со списком песен: ")

tracks = []

with open(list_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            left = line.split("[")[0].strip()
            number, title = left.split(". ", 1)
            tracks.append((number, title))

files = os.listdir(music_dir)

for number, title in tracks:
    for filename in files:
        name, ext = os.path.splitext(filename)
        if name.strip().lower() == title.strip().lower():
            old_path = os.path.join(music_dir, filename)
            new_name = number + ". " + title + ext
            new_path = os.path.join(music_dir, new_name)
            os.rename(old_path, new_path)
            print(filename, "->", new_name)
            break