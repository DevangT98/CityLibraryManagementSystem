import mysql.connector
import datetime

class SqlConnection:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="librarydb_2"
        )

        self.cursor = self.conn.cursor()


    def insert_reader(self, card_no, rtype, name, addr, phone):
        query = """INSERT INTO reader VALUES(%s,%s,%s,%s,%s) """
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
        query = "SELECT reader.RID, reader.RNAME, COUNT(BOR_NO) FROM borrows INNER JOIN reader ON borrows.RID=reader.RID INNER JOIN book ON book.DOCID=borrows.DOCID GROUP BY borrows.RID ORDER BY COUNT(BOR_NO) desc LIMIT %s"
        data =(n,)
        self.cursor.execute(query,data)  
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
        record = (n,)
        self.cursor.execute(query,record)  
        row = self.cursor.fetchall()
        return row
    
    def show_branch_most_borrowed_books(self,n,branch_id): 
        query = "SELECT book.DOCID, document.TITLE,COUNT(BOR_NO) FROM borrows INNER JOIN reader ON borrows.RID=reader.RID INNER JOIN branch ON borrows.BID= branch.BID INNER JOIN book ON book.DOCID=borrows.DOCID INNER JOIN document ON document.DOCID=book.DOCID WHERE branch.BID=%s GROUP BY branch.BID ORDER BY COUNT(BOR_NO) desc LIMIT %s"
        record = (branch_id,n)
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
            return True,id

    def get_doc_details(self,reader_value,search_selection_type):

        if search_selection_type == 'TITLE':    
            query = f"SELECT d.DOCID, d.TITLE,d.PDATE,p.PUBNAME FROM document d INNER JOIN publisher p on d.PUBLISHERID=p.PUBLISHERID where TITLE LIKE '%{reader_value}%'" 
            self.cursor.execute(query)
            #record=(reader_value,)
        elif search_selection_type == 'PUBNAME':
            query = f"SELECT d.DOCID, d.TITLE,d.PDATE,p.PUBNAME FROM document d INNER JOIN publisher p on d.PUBLISHERID=p.PUBLISHERID where p.PUBNAME LIKE '%{reader_value}%'"
            #record = (reader_value,)
            self.cursor.execute(query)
        else:
            query = "SELECT d.DOCID, d.TITLE,d.PDATE,p.PUBNAME FROM document d INNER JOIN publisher p on d.PUBLISHERID=p.PUBLISHERID where d.docID=%s"
            record = (int(reader_value),)
            self.cursor.execute(query,record)

        row = self.cursor.fetchall()
        return row

    def show_all_documents(self):
        #query = "SELECT d.DOCID, d.TITLE,d.PDATE,p.PUBNAME FROM document d INNER JOIN publisher p on d.PUBLISHERID=p.PUBLISHERID"
        query ="SELECT d.DOCID, d.TITLE,c.COPYNO,c.CPY_POSITION,c.BID,d.PDATE,p.PUBNAME FROM document d INNER JOIN publisher p on d.PUBLISHERID=p.PUBLISHERID INNER JOIN copy_cpyno c ON d.DOCID = c.DOCID"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row
    
    def insert_document(self,docid,copyno,branchid,copypos):
        if not self.check_copy(docid,copyno,branchid):
            query = """INSERT INTO copy_cpyno VALUES(%s,%s,%s,%s)"""
            record = (docid,copyno,branchid,copypos)

            try:
                self.cursor.execute(query, record)
                self.conn.commit()
                print("Insert successful!!....")
                return True
            except Exception as e:

                self.conn.rollback()
                print("Insert Failed!!....", e)

        else:
            return False        
        self.conn.close()

    def check_copy(self,doc_id,copy_no,branch_id):
        query = "SELECT * from copy_cpyno where DOCID=%s and COPYNO=%s and BID=%s"
        record=(doc_id,copy_no,branch_id)
        self.cursor.execute(query,record)
        row = self.cursor.fetchall()

        if not row:
            return False
        else:
            return True

    
    def get_doc_ids(self):
        query = 'SELECT DOCID from DOCUMENT order by DOCID'
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row

    def insert_in_borrowings(self,bor_no,doc_id,copy_no,branch_id,reader_id,time):
      
        query1 = "INSERT INTO borrowing VALUES (%s,%s,%s)"

        record = (bor_no,time,None)
        query2 = f"INSERT INTO borrows VALUES ({int(bor_no)},{int(doc_id)},{int(copy_no)},{int(branch_id)},{int(reader_id)})"

        try:
            self.cursor.execute(query1,record)
            self.conn.commit()
            print(" 1 Insert successful!!....")
            self.cursor.execute(query2)
            self.conn.commit()
            print("2 Insert successful!!....")
            return True

        except Exception as e:

            self.conn.rollback()
            print("Insert Failed!!....", e)
    

    def insert_in_reserves(self,res_no,doc_id,copy_no,branch_id,reader_id,formatted_date):
        query1 = "INSERT INTO reservation VALUES (%s,%s)"

        record = (res_no,formatted_date)
        query2 = f"INSERT INTO RESERVES VALUES ({int(reader_id)},{int(res_no)},{int(doc_id)},{int(copy_no)},{int(branch_id)})"

        try:
            
            self.cursor.execute(query1,record)
            self.conn.commit()
            print(" 1 Insert successful!!....")
            self.cursor.execute(query2)
            self.conn.commit()
            print("2 Insert successful!!....")
            return True

        except Exception as e:

            self.conn.rollback()
            print("Insert Failed!!....", e)
        
    def return_book_sql(self,bor_no,formatted_date):
        
        query1 = f"UPDATE borrowing set RDTIME='{formatted_date}' where BOR_NO={bor_no}"
        try:
            self.cursor.execute(query1)
            self.conn.commit()
        except Exception as e:

            self.conn.rollback()
            print("Insert Failed!!....", e)
    def show_borrowed_docs(self):
        query ="SELECT bo.bor_no,bo.bdtime,d.title,b.copyno,c.docid,b.bid FROM BORROWS b INNER JOIN COPY C on c.docid = b.docid and c.copyno = b.copyno and b.bid = c.bid INNER JOIN document d on d.docid = c.docid INNER JOIN borrowing bo on b.bor_no = bo.bor_no where bo.rdtime is NULL"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row  
    
    def fetch_bor_ret_date(self):
        query = "SELECT bdtime, rdtime from borrowing where bor_no="