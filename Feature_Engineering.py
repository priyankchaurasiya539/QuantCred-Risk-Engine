import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),  
    database="bnpl_db"
)

df = pd.read_sql("SELECT * FROM user_scoredcard_data", mydb)
mydb.close()  
print(df.head(10))
print("-" * 100)

#Columns 
print(df.columns)
print("-" * 100)

#Shape 
print("Shape : " , df.shape)
print("-" * 100)

#Info
print(df.info())
print("-" * 100)


#Correlation
print(df.corr())
print("-" * 100)

#Saving the cleaned dataset into csv file 
df.to_csv("data/QuantCred.csv")
print("Data saved successfully.")

"""Visulalization"""

#It will represent the distribution of CIBIL score with will_default

plt.figure(figsize=(8, 5))
sns.boxplot(x='Will_Default', y='CIBIL_Score', data=df, palette='Set2')
plt.title('CIBIL Score Distribution by Default Risk')
plt.xlabel('Will Default')
plt.ylabel('CIBIL Score')
plt.xticks([0 , 1 ] , ["Safe" , "Defaulter"] ,rotation= 0)
plt.savefig("Graphs/CIBIL_score and Will Default.png")
plt.show()


#Correlation heatmap

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Customer Profile Data')
plt.tight_layout()
plt.savefig("Graphs/Correlation Heatmap.png")
plt.show()

#Montly App orders
plt.figure(figsize=(8 , 6 ))
sns.histplot(df['Monthly_App_Orders'], bins=20, kde=True, color='coral')
plt.title('Distribution of Monthly App Orders across Users')
plt.xlabel('Number of Monthly Orders')
plt.ylabel('User Count')
plt.grid(axis='y', alpha=0.6)
plt.savefig("Graphs/Monthly App Orders.png")
plt.show()