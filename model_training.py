import pandas as pd
import joblib 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import  r2_score , accuracy_score 
from sklearn.linear_model import LinearRegression , LogisticRegression , Ridge 
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/QuantCred.csv")
print(df.head(10))


#Now splitting the independent and dependent features for the model training 
X = df.drop(columns=["User_Id" , "Will_Default" , "Allocated_Credit_Limit" , "Unnamed: 0"])
y1 = df["Will_Default"]
y2 = df["Allocated_Credit_Limit"]


"""Logistic Regression"""

#Train_test_split(For Logistic Regression)
X_train_clf , X_test_clf , y1_train , y1_test = train_test_split(X , y1 , test_size=0.25 , random_state=42 ,stratify=  y1)

#Apply standardisation for classification
scaler_clf = StandardScaler()
X_train_clf_scaled = scaler_clf.fit_transform(X_train_clf)
X_test_clf_scaled = scaler_clf.transform(X_test_clf)

"""Ridge Regression"""
#Filtering : - Put the safe users data only 

safe_users_mask = (df["Will_Default"] == 0 )  #Safe users

X_reg = X[safe_users_mask]
y2_reg = y2[safe_users_mask]

#Train_test_split(For Ridge Regression)
X_train_reg , X_test_reg , y2_train , y2_test = train_test_split(X_reg , y2_reg , test_size=0.25 , random_state=42)


#Apply standardization for Ridge Regression
scaler_reg = StandardScaler()
X_train_reg_scaled = scaler_reg.fit_transform(X_train_reg)
X_test_reg_scaled = scaler_reg.transform(X_test_reg)


"""Train the models"""

#For classification
classifier = LogisticRegression()
classifier.fit(X_train_clf_scaled , y1_train)


#For regression 
regression = Ridge(alpha=1.0)
regression.fit(X_train_reg_scaled , y2_train)

"""Accuracies of both models"""
y1_pred = classifier.predict(X_test_clf_scaled)
clf_acu = accuracy_score(y1_test , y1_pred)
print("Classification accuracy : " , round(clf_acu * 100 , 2) )

y2_pred = regression.predict(X_test_reg_scaled)
reg_accu = r2_score(y2_test ,y2_pred)
print("Regression accuracy : " , round(reg_accu * 100 , 2) )



"""Saving the models using joblib"""

#Saving the classification scaler and Regression scaler
joblib.dump(scaler_clf , "models/scaler_clf.pkl")
joblib.dump(scaler_reg , "models/scaler_reg.pkl")

#saving the models file 
joblib.dump(classifier , "models/logistic_model.pkl")
joblib.dump(regression , "models/ridge_model.pkl")


print("QuantCred Pipeline Built Successfully! All artifacts are saved.")



