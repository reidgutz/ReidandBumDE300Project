import pandas as pd

data = pd.read_csv('data/heart_disease.csv')
data = data.iloc[:899, :]

keep_list = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
data = data.iloc[:899, :]
data = data.loc[:, keep_list]

data.to_csv("data/cleaned_data.csv")