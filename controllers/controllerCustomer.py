from models import User
from database.config import config
import psycopg2

def addCustomer(User):
    sql = """INSERT INTO customers(email,password,nickname)
             VALUES(%s,%s,%s);"""
    conn = None
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
       
        cur.execute(sql, (User.email,User.password,User.nickname))
        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
def deleteCustomer(User):
    conn = None
    rows_deleted = 0
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM customers WHERE id = %s", (User.id))
        rows_deleted = cur.rowcount
      
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

def updateCustomer(User):
    sql = """ UPDATE customers
                SET nickname = %s, password = %s
                WHERE email = %s"""
    conn = None
    updated_rows = 0
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(sql, (User.nickname,User.password,User.email))
        updated_rows = cur.rowcount
        
        conn.commit()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

    
def showCustomer(User):
 
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT id,nickname, FROM customers ORDER BY id")
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()