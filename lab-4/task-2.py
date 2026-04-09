import sqlite3
import hashlib

db = sqlite3.connect("library.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(login TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS authors(id INTEGER PRIMARY KEY, name TEXT, country TEXT, years TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, author_id INTEGER, title TEXT)")

login = input("Логин: ")
password = hashlib.md5(input("Пароль: ").encode()).hexdigest()

cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))

if cursor.fetchone():
    print("Вход выполнен")
else:
    print("Нет пользователя")