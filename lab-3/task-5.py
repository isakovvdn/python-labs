import tkinter as tk

def format_text():
    text = entry.get()

    if var_remove.get():
        words = text.split()
        text = " ".join([w for w in words if len(w) >= int(entry_n.get())])

    if var_digits.get():
        text = "".join(['*' if c.isdigit() else c for c in text])

    if var_spaces.get():
        text = " ".join(list(text))

    if var_sort_len.get():
        text = " ".join(sorted(text.split(), key=len))

    if var_sort_lex.get():
        text = " ".join(sorted(text.split()))

    result.delete(0, tk.END)
    result.insert(0, text)


root = tk.Tk()
root.title("StringFormatter")

entry = tk.Entry(root, width=50)
entry.pack()

entry_n = tk.Entry(root, width=5)
entry_n.insert(0, "5")
entry_n.pack()

var_remove = tk.BooleanVar()
tk.Checkbutton(root, text="Удалить короткие слова", variable=var_remove).pack()

var_digits = tk.BooleanVar()
tk.Checkbutton(root, text="Заменить цифры", variable=var_digits).pack()

var_spaces = tk.BooleanVar()
tk.Checkbutton(root, text="Добавить пробелы", variable=var_spaces).pack()

var_sort_len = tk.BooleanVar()
tk.Checkbutton(root, text="Сортировка по длине", variable=var_sort_len).pack()

var_sort_lex = tk.BooleanVar()
tk.Checkbutton(root, text="Сортировка лексикографически", variable=var_sort_lex).pack()

tk.Button(root, text="Форматировать", command=format_text).pack()

result = tk.Entry(root, width=50)
result.pack()

root.mainloop()