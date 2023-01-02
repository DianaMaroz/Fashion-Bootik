import sqlite3

conn = sqlite3.connect(r'data_base/bot_db.db')
cur = conn.cursor()

def check_connection():
    global conn
    global cur
    conn = sqlite3.connect(r'data_base/bot_db.db')
    cur = conn.cursor()
    create_table()

def create_table():
    global conn
    global cur
    new_table = '''CREATE TABLE IF NOT EXISTS goods (id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT, image TEXT, name TEXT, description TEXT, size TEXT, quantity INTEGER,
    price REAL)'''
    cur.execute(new_table)
    conn.commit()

def new_item(item: dict):
    global conn
    global cur
    goods = (item.get('type'), item.get('image'), item.get('name'),
             item.get('description'), ' '.join(list(map(str, item.get('size')))), item.get('quantity'),
             item.get('price'))
    print(goods)
    new_item = '''INSERT INTO goods (type, image, name, description, size,
    quantity, price) VALUES (?, ?, ?, ?, ?, ?, ?)'''
    cur.execute(new_item, goods)
    conn.commit()

def get_item(g_type: str):
    global conn
    global cur
    get = ('''SELECT name FROM goods WHERE type=?''')
    result = cur.execute(get, (g_type, )).fetchall()
    conn.commit()
    return result
