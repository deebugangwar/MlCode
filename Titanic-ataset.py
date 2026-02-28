from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data = pd.read_csv("/content/Titanic-Dataset.csv")


data = data[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]


data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])


categorical_cols = ['Sex', 'Embarked']
numerical_cols = ['Pclass','Age','SibSp','Parch','Fare']


encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded_data = encoder.fit_transform(data[categorical_cols])


encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols))


X = pd.concat([data[numerical_cols], encoded_df], axis=1)
y = data['Survived']


model = LogisticRegression(max_iter=1000)


kf = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print("Fold Accuracies:", scores)
print("Average Accuracy:", scores.mean())
