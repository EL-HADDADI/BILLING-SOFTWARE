import sqlite3


def connect():
    try:
        con = sqlite3.connect("db/mini_database.db")
        print("connected")
        con.commit()

    except:
        print("failed to connect")
        con.close()


def insertRecord(id, name, phone, total, product):
    try:
        con = sqlite3.connect("db/mini_database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO store VALUES(?,?,?,?,?)", (id, name, phone, total, product))
        con.commit()
        print("stored")

    except:
        print("failed")






