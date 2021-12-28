import sqlite3


def connect():
    con = sqlite3.connect("flashCardDatabase.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flashCardDB (info TEXT)
        """)
    con.commit()
    con.close()


def ADD(info):
    con = sqlite3.connect("flashCardDatabase.db")
    cur = con.cursor()
    cur.execute("""
        INSERT INTO flashCardDB VALUES (?)
        """, (info,))
    con.commit()
    con.close()


def VIEW():
    con = sqlite3.connect("flashCardDatabase.db")
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM flashCardDB
        """)
    row = cur.fetchall()
    con.close()
    return row


def DELETE_ALL():
    con = sqlite3.connect("flashCardDatabase.db")
    cur = con.cursor()
    cur.execute("""
        DELETE FROM flashCardDB
        """)
    con.commit()
    con.close()


def DELETE(info):
    con = sqlite3.connect("flashCardDatabase.db")
    cur = con.cursor()
    cur.execute("""
        DELETE FROM flashCardDB WHERE info=?
        """, (info,))
    con.commit()
    con.close()


connect()