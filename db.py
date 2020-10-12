import sqlite3 as sql

connection = sql.connect('buffer.sqlite')
db = connection.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS buffer (var TEXT, val TEXT)''')
connection.commit()

def get():
    _tx = {}
    db.execute("SELECT * FROM buffer")
    row = db.fetchone()

    while row is not None:
        _tx[row[0]] = row[1]
        row = db.fetchone()
    return _tx

def set(idx, _tx):
    #ret = db.execute("UPDATE buffer IF EXISTS SET val='" + _tx + "' WHERE var='" + idx + "';")
    #connection.commit()

    db.execute("INSERT INTO buffer (var, val) VALUES ('" + idx + "', '" + _tx + "')")
    connection.commit()

def dlt(idx):
    db.execute("DELETE FROM buffer WHERE var='" + idx + "'")
    connection.commit()
