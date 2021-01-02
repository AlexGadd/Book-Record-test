import sqlite3

file_name = "data.db"


def load_all():
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='book_list'")
    print(cursor.fetchall())
    if not cursor.fetchall():
        create_book_list()
    cursor.execute("SELECT rowid, * FROM book_list")
    return cursor.fetchall()
    conn.close()


def load_current():
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM book_list WHERE current='True'")
    return cursor.fetchall()
    conn.close()


def save(arg):
    pass


def create_book_list():
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS book_list (
    		title text NOT NULL,
    		author text NOT NULL,
    		length integer NOT NULL,
    		target_date integer NOT NULL,
    		current text NOT NULL,
    		position integer DEFAULT 0
    		)""")
    conn.commit()
    conn.close()


load_all()
