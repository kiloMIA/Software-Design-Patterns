from models import Product
from database.config import config
import psycopg2

def addProduct():
    sql = """INSERT INTO products(name,price)
             VALUES(%s,%s);"""
    conn = None
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
       
        cur.execute(sql, (Product.name,Product.price))
        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
def deleteProduct():
    conn = None
    rows_deleted = 0
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM prodcuts WHERE id = %s", (Product.id))
        rows_deleted = cur.rowcount
      
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

def updateProduct():
    sql = """ UPDATE products
                SET name = %s, price = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(sql, (Product.name,Product.price,Product.id))
        updated_rows = cur.rowcount
        
        conn.commit()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

    
def showProduct():
 
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT id,name, FROM products ORDER BY id")
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