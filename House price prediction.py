from sklearn.linear_model import LinearRegression
import pandas as pd
df=pd.read_csv("/content/Housing.csv")
df
y = df["price"]
x =df.drop("price",axis=1)
x=pd.get_dummies(x,drop_first=True)
x
model = LinearRegression()
model.fit(x,y)
new_house = [[
    3000, 3, 2, 2,5,4,7,23,6,8,4,3,2
   
]]

price_prediction = model.predict(new_house)
print("Predicted House Price:", price_prediction)
