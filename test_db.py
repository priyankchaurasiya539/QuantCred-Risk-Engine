import mysql.connector

try:
    # 1. Connection object taiyar karo
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="157565",
        database="bnpl_db"
    )
    
    # 2. Check karo connection successful hua ya nahi
    if mydb.is_connected():
        print("🎉 Connection Successful! Python and MySQL are now linked.")
        
    mydb.close()

except Exception as e:
    print("❌ Error while connecting to MySQL:", e)