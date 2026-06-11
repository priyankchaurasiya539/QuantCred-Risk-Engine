import mysql.connector
import random   #Generating the random data 

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
        print("Connection Successful! Python and MySQL are now linked.")
    
    cursor = mydb.cursor()
    for i in range ( 1000 ):
        Monthly_App_Orders = random.randint(2 , 50)
        Average_Order_Value = round(random.uniform(150.0 , 2000.0) , 2)
        Account_Age_Months = random.randint(1 , 60)
        Delayed_Payments_Count = random.randint( 0 , 10 )
        CIBIL_score = random.randint(300 , 900)
        Monthly_Income_Lakhs = round(random.uniform(0.3 , 4.0) , 2)

        if Delayed_Payments_Count > 3 or CIBIL_score < 650 :
            Will_Default = 1 
        
        else :
            Will_Default = 0

        if Will_Default == 1 :
            Allocated_Credit_Limit = 0 
        else :
            base_calc = (CIBIL_score * 10) + (Monthly_Income_Lakhs * 2000)
            
            #Adding some noise to make a data to a real world level
            random_noise = random.randint(-1500, 1500)
            Allocated_Credit_Limit = base_calc + random_noise
            
            
            Allocated_Credit_Limit = round(max(500, Allocated_Credit_Limit), 0)


        query = """
        INSERT INTO user_scoredcard_data (
            Monthly_App_Orders, Average_Order_Value, Account_Age_Months, 
            Delayed_Payments_Count, CIBIL_Score, Monthly_Income_Lakhs, 
            Will_Default, Allocated_Credit_Limit
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            Monthly_App_Orders, Average_Order_Value, Account_Age_Months, 
            Delayed_Payments_Count, CIBIL_score, Monthly_Income_Lakhs, 
            Will_Default, int(Allocated_Credit_Limit)
        )
        
        cursor.execute(query, values)

    mydb.commit()
    mydb.close()

except Exception as e:
    print("Error while connecting to MySQL:", e)


