import mysql.connector


class SqlConnection:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="librarydb"
        )

        self.cursor = self.conn.cursor()


    def insert_reader(self, card_no, rtype, name, addr, phone):
        query = """INSERT INTO librarydb.reader VALUES(%s,%s,%s,%s,%s) """
        record = (card_no, rtype, name, addr, phone)
        try:
            self.cursor.execute(query, record)
            self.conn.commit()
            print("Insert successful!!....")
        except Exception as e:

            self.conn.rollback()
            print("Insert Failed!!....", e)

        
        self.conn.close()

    def show_branch_details(self):
        query = "SELECT LNAME,LOCATION FROM branch"
        self.cursor.execute(query)  
        row = self.cursor.fetchall()
        return row

    def show_most_frequent_borrowers(self,n):
        query = "SELECT reader.RID, reader.RNAME, COUNT(BOR_NO),FROM borrows INNER JOIN reader ON borrows.RID=reader.RID INNER JOIN book ON book.DOCID=borrows.DOCID GROUP BY borrows.RID ORDER BY COUNT(BOR_NO) desc LIMIT %s"
        self.cursor.execute(query,n)  
        row = self.cursor.fetchall()
        return row
    
    def show_branch_most_frequenct_borrowers(self,n,branch_id):
        query = "SELECT reader.RID, reader.RNAME, branch.BID, branch.LNAME, COUNT(BOR_NO) FROM borrows INNER JOIN reader ON borrows.RID=reader.RID INNER JOIN branch ON borrows.BID=branch.BID INNER JOIN book ON book.DOCID=borrows.DOCID WHERE branch.BID=%s GROUP BY borrows.RID ORDER BY COUNT(BOR_NO) desc LIMIT %s"
        record = (branch_id,n)
        self.cursor.execute(query,record)  
        row = self.cursor.fetchall()
        return row
    
    def show_most_borrowed_books(self,n):
        query = "SELECT book.DOCID, document.TITLE FROM borrows INNER JOIN book ON borrows.DOCID=book.DOCID INNER JOIN document ON borrows.DOCID=document.DOCID GROUP BY BOR_NO ORDER BY COUNT(BOR_NO) DESC LIMIT %s"
        record = (n)
        self.cursor.execute(query,record)  
        row = self.cursor.fetchall()
        return row
    
    #NEED TO JOIN WITH DOC
    def show_branch_most_borrowed_books(self,n,branch_id): 
        query = "SELECT book.DOCID, document.TITLE FROM borrows INNER JOIN reader ON borrows.RID=reader.RID INNER JOIN branch ON borrows.BID= branch.BID INNER JOIN book ON book.DOCID=borrows.DOCID WHERE branch.BID=%s GROUP BY branch.BID ORDER BY COUNT(BOR_NO) desc LIMIT %s"
        record = (n,branch_id)
        self.cursor.execute(query,record)  
        row = self.cursor.fetchall()
        return row

    def validate_admin(self,id,password):
         query = "SELECT id, password from admin_table where id=%s and password=%s"
         data = (id,password)
         self.cursor.execute(query,data)
         row = self.cursor.fetchall()
         if not row:
            return False
         else:
            return True

    def validate_reader(self,id):
        query = "SELECT rid from reader where rid=%s"
        data = (id,)
        self.cursor.execute(query,data)
        row = self.cursor.fetchall()
        if not row:
            return False
        else:
            return True
