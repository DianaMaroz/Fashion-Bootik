import sqlite3

conn = sqlite3.connect(r'data_base/bot_db.db')
cur = conn.cursor()

def check_connection():
    global conn
    global cur
    conn = sqlite3.connect(r'data_base/bot_db.db')
    cur = conn.cursor()
    create_goods_table()
    create_basket_table()

def create_goods_table():
    global conn
    global cur
    new_table = '''CREATE TABLE IF NOT EXISTS goods (id INTEGER PRIMARY KEY AUTOINCREMENT,
    g_type TEXT, image TEXT, name TEXT, desc TEXT, quantity INTEGER, price REAL)'''
    cur.execute(new_table)
    conn.commit()

def new_item(item: dict):
    global conn
    global cur
    goods = (item.get('g_type'), item.get('image'), item.get('name'),
             item.get('desc'), item.get('quantity'), item.get('price'))
    print(goods)
    new_item = '''INSERT INTO goods (g_type, image, name, desc,
    quantity, price) VALUES (?, ?, ?, ?, ?, ?)'''
    cur.execute(new_item, goods)
    conn.commit()

def get_item(g_type: str):
    global conn
    global cur
    get = (f'SELECT * FROM goods WHERE g_type=?')
    result = cur.execute(get, (g_type, )).fetchall()
    conn.commit()
    return result

def get_by_id(g_id: int):
    global conn
    global cur
    get = ('SELECT * FROM goods WHERE id=?')
    result = cur.execute(get, (g_id, )).fetchone()
    conn.commit()
    return result


def set_count(g_id: int, increase: int):
    global conn
    global cur
    get = '''SELECT quantity FROM goods WHERE id=?'''
    result = int(cur.execute(get, (g_id, )).fetchone()[0])
    count = '''UPDATE goods SET quantity=? WHERE id=?'''
    if result == 0:
        return False
    else:
        cur.execute(count, (result + increase, g_id))
    conn.commit()
    return result


def create_basket_table():
    global conn
    global cur
    new_table = '''CREATE TABLE IF NOT EXISTS basket (id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER, id_good INTEGER)'''
    cur.execute(new_table)
    conn.commit()

def add_to_basket(id_user: int, id_goods: int):
    global conn
    global cur
    add_basket = '''INSERT INTO basket (id_user, id_good) VALUES (?, ?)'''
    cur.execute(add_basket, (id_user, id_goods, ))
    conn.commit()

def remove_from_basket(id_user: int, id_goods: int):
    global conn
    global cur
    remove_basket = '''DELETE FROM basket WHERE id_user=? AND id_good=?'''
    cur.execute(remove_basket, (id_user, id_goods, ))
    conn.commit()

def get_basket(id_user: int):
    global conn
    global cur
    get = ('''SELECT * FROM basket WHERE id_user=?''')
    result = cur.execute(get, (id_user,)).fetchall()
    conn.commit()
    return result
