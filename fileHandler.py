import sqlite3

file_name = "data.db"


def load_all():
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='book_list'")
    if not cursor.fetchall():
        create_book_list()
    cursor.execute("SELECT rowid, * FROM book_list")
    result = cursor.fetchall()
    conn.close()
    return result


def load_current():
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM book_list WHERE current='True'")
    result = cursor.fetchall()
    conn.close()
    return result


def load_finished():
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM book_list WHERE current='False'")
    result = cursor.fetchall()
    conn.close()
    return result


def save(record):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book_list VALUES (?,?,?,?,?,?)", record)
    conn.commit()
    conn.close()


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


def add_new_position(rowid, page):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE book_list SET position=(?) WHERE rowid=(?)", (page, rowid))
    conn.commit()
    conn.close()


def change_to_complete(rowid):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE book_list SET current='False' WHERE rowid=(?)", (rowid,))
    conn.commit()
    conn.close()
