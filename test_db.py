import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="bnpl_db"
    )
    
    if mydb.is_connected():
        print(" Connection Successful! Python and MySQL are now linked.")
        
    mydb.close()

except Exception as e:
    print("Error while connecting to MySQL:", e)