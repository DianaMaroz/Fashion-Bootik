import sqlite3


class DataBase:
    def __init__(self, db_path: str = 'data_base/bot_db.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_goods(self):
        sql = '''CREATE TABLE IF NOT EXISTS goods 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        g_type TEXT, image TEXT, name TEXT, 
        desc TEXT, quantity INTEGER, price REAL)'''
        self.execute(sql, commit=True)

    def create_table_basket(self):
        sql = '''CREATE TABLE IF NOT EXISTS basket 
        (id_order INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER, id_good INTEGER)'''
        self.execute(sql, commit=True)

    def add_goods(self, goods: dict):
        parameters = (goods.get('g_type'), goods.get('image'), goods.get('name'),
                      goods.get('desc'), goods.get('quantity'), goods.get('price'))
        sql = '''INSERT INTO goods (g_type, image, name, desc, quantity, price) 
        VALUES (?, ?, ?, ?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_goods(self, **kwargs):
        sql = '''SELECT * FROM goods WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def get_basket(self, **kwargs):
        sql = '''SELECT * FROM basket WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def remove_from_basket(self, **kwargs):
        sql = '''SELECT * FROM basket WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)


    def set_count(self, id_item: int, increase: bool):
        if increase:
            sql = '''UPDATE goods SET quantity = quantity + 1 WHERE id=?'''
        else:
            sql = '''UPDATE goods SET quantity = quantity - 1 WHERE id=?'''
        self.execute(sql, (id_item,))

    @staticmethod
    def extract_kwargs(sql, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()
