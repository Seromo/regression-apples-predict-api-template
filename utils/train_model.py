"""
    Simple file to create a Sklearn model for deployment in our API

    Author: Explore Data Science Academy

    Description: This script is responsible for training a simple linear
    regression model which is used within the API for initial demonstration
    purposes.

"""

# Dependencies
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Fetch training data and preprocess for modeling
train = pd.read_csv('data/train_data.csv')

train = train[(train['Commodities'] == 'APPLE GOLDEN DELICIOUS')]


y_train = train['avg_price_per_kg']
X_train = train[['Total_Qty_Sold','Weight_Kg','Stock_On_Hand','Low_Price', 'High_Price','Sales_Total','Total_Kg_Sold']]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Fit model
lm_regression = LinearRegression(normalize=True)
print ("Training Model...")
lm_regression.fit(X_train, y_train)



#RF = RandomForestRegressor(n_estimators=100, max_depth=20, random_state=23)
#RF.fit(X_train,y_train)

# Pickle model for use within our API
save_path = '../assets/trained-models/LR.pkl'
print (f"Training completed. Saving model to: {save_path}")
pickle.dump(lm_regression, open(save_path,'wb'))
