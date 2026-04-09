import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.title("Поиск строк")

listbox = tk.Listbox(root, width=80, height=20)
listbox.pack(fill=tk.BOTH, expand=True)


def open_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            for match in re.finditer(r"\d{2}-\d{2}-\d{4}", line):
                text = f"Строка {i}, позиция {match.start()+1}: {match.group()}"
                listbox.insert(tk.END, text)


menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)

root.mainloop()