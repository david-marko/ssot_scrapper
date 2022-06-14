import os
import mysql.connector

db_host = os.environ['db_host']
db_user = os.environ['db_user']
db_pass = os.environ['db_pass']
db_name = os.environ['db_name']


def insert(sql):
    conn = mysql.connector.connect(host=db_host,user=db_user,port=3306, password=db_pass,database=db_name)
    # Create a cursor to execute the python file
    cursor = conn.cursor(dictionary=True,buffered=True)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print("Script couldnt execute")
        pass

