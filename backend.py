import sqlite3


class Database():
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self): 
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        
    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
        self.conn.commit()
    
    def search(self,title="", author = "", year = 0, isbn = 0):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        
        return rows

    def __del__(self):
        self.conn.close()

# def search(title="", author = "", year = 0, isbn = 0):
#     conn = sqlite3.connect("book.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM book WHERE title LIKE '%'?'%' OR author LIKE %?% OR year LIKE %?% OR isbn LIKE %?%",(title, author, year, isbn))
#     rows = cur.fetchall()
#     conn.close()

#     return rows


# insert("Holy Crap", "Monkey King", 4561, 78946)
# delete(1)


# insert("Banana Land", "Monkey King", 4561, 78946)
# insert("Monster Ball", "Lunatic", 1961, 78445)
# insert("Manly Gayle", "Universe Boss", 2015, 78656)

# print(view())
