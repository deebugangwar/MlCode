import pandas as pd


data = {'City': ['Delhi', 'Mumbai', 'Bangalore'], 'Price': [100, 150, 120]}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

df_dummies = pd.get_dummies(df, columns=['City'], drop_first=False)

print("\nDummy Variable Data:")
print(df_dummies)
