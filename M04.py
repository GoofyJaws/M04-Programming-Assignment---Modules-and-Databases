import sqlite3

def connect():
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(title text,author text,year integer)")
    print("here1")
    conn.commit()
    conn.close()

def insert(title,author,year):
    conn = sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?)",(title,author,year))
    print("here2")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    for row in cur.execute("SELECT *FROM book"):
        print(row)
    return rows
    conn.close()

def delete(year):
    conn = sqlite3.connect("books2.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE year=?",(year,))
    conn.commit()
    conn.close()

connect()

#insert('The Weirdstone of Brisingamen', 'Alan Garner', 1960)
#insert('Perdido Street Station', 'China Miéville', 2000)
#insert('Thud!', 'Terry Pratchett', 2005)
#insert('The Spellman Files', 'Lisa Lutz', 2007)
#insert('Small Gods', 'Terry Pratchett', 1992)



#delete(1992)
print(view())
