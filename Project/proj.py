import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from scipy import stats
from scipy.stats import kurtosis, skew
from sqlalchemy import create_engine
import psycopg2

plt.rcParams.update(**{'figure.dpi':150})
plt.style.use('ggplot') 

conn_string = 'postgresql://postgres:de300hardpassword@localhost:5432/heart'
db = create_engine(conn_string)
data = pd.read_sql_query('SELECT * FROM heart_data', con = db)

#data = pd.read_csv('data/heart_disease.csv')

# Part 3
miss_dict = {}
keep_list = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
data = data.iloc[:899, :]
data = data.loc[:, keep_list]
for i in data.columns:
    miss_dict[i] = data[i].isnull().sum()

print(miss_dict)



# trestbps - mean imputation, data already looks normal
# chol - resampling, bimodal data thus KNN is better than mean 
# fbs - KNN, categorical with a decent number of missing values, KNN handles this best
# restecg - mode (0) only 2 missing
# thalach - mean imputation, approx normal
# exang - KNN, categorical with a decent number of missing values, KNN handles this best
# oldpeak - resampling, bimodal data thus KNN is better than mean
# slope - KNN, too many values missing so no viable alternatives
# ca - KNN, too many values missing so no viable alternatives
# thal - KNN, too many values missing so no viable alternatives

imputer = KNNImputer(n_neighbors=3)
column_to_impute = ['chol', 'fbs', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
data_imputed = data.copy()
data_imputed[column_to_impute] = imputer.fit_transform(data[column_to_impute])
data_imputed['trestbps'] = data_imputed['trestbps'].fillna(np.mean(data['trestbps']))
data_imputed['thalach'] = data_imputed['thalach'].fillna(np.mean(data['thalach']))
data_imputed['restecg'] = data_imputed['restecg'].fillna(0)

data_imputed['age'] = data_imputed['age'].astype(float)


# Part 4
fig,axs = plt.subplots(2,3,figsize=(16,8))

_ = sns.boxplot(data_imputed,y='age',ax=axs[0,0],width=.5)
_ = sns.boxplot(data_imputed,y='trestbps',ax=axs[0,1],width=.5)
_ = sns.boxplot(data_imputed,y='chol',ax=axs[0,2],width=.5)
_ = sns.boxplot(data_imputed,y='thalach',ax=axs[1,0],width=.5)
_ = sns.boxplot(data_imputed,y='oldpeak',ax=axs[1,1],width=.5)

fig.tight_layout()
plt.savefig(f"boxplot_of_numerical_features_pre_outlier_removal.jpg")

# From inspection, resting heart rate being at 0 makes no sense, thus we decided to remove the lowest valued outliers for the
# trest column. Similarly, cholesterol level being too low did not make sense, thus we removed the lowest valued outliers. We
# chose to keep the higher valued outliers because this dataset is one for heart disease patients, thus having an extremely high
# resting heart rate or cholesterol which would normally be outliers are not necessarily outliers for this dataset. 

# Check if 0 cholesterol would be considered outliers  
columns = ['trestbps', 'chol']
for i in columns:
    #Identify outliers
    q1 = data_imputed[i].quantile(0.25)
    q3 = data_imputed[i].quantile(0.75)
    iqr = q3 - q1
    if i == 'trestbps':
        lbound = q1 - 2 * iqr
    else:
        lbound = q1 - 1.5 * iqr
    data_imputed = data_imputed[(data_imputed[i] >= lbound)]

fig,axs = plt.subplots(2,3,figsize=(16,8))

_ = sns.boxplot(data_imputed,y='age',ax=axs[0,0],width=.5)
_ = sns.boxplot(data_imputed,y='trestbps',ax=axs[0,1],width=.5)
_ = sns.boxplot(data_imputed,y='chol',ax=axs[0,2],width=.5)
_ = sns.boxplot(data_imputed,y='thalach',ax=axs[1,0],width=.5)
_ = sns.boxplot(data_imputed,y='oldpeak',ax=axs[1,1],width=.5)

fig.tight_layout()
plt.savefig(f"boxplot_of_numerical_features_post_outlier_removal.jpg")

# Part 5
for column in ['age','trestbps','chol','thalach','oldpeak']:
    minimum = data_imputed[column].min()
    maximum = data_imputed[column].max()
    mean = data_imputed[column].mean()
    q1, q2, q3 = data_imputed[column].quantile([0.25, 0.5, 0.75])
    kur = kurtosis(data_imputed[column])
    skw = skew(data_imputed[column])
    
    # print the summary statistics
    print("Column name: ", column)
    print("Minimum value: ", minimum)
    print("First quartile (Q1): ", q1)
    print("Median (Q2): ", q2)
    print("Third quartile (Q3): ", q3)
    print("Maximum value: ", maximum)
    print("Mean: ", mean)
    print("Kurtosis: ", kur)
    print("Skewness: ", skw)

# Part 6
fig,axs = plt.subplots(2,3,figsize=(16,8))
_ = sns.histplot(data_imputed, x = 'exang', ax = axs[0,0], bins = 10)

_ = sns.histplot(data_imputed, x = 'oldpeak', ax = axs[0,1], bins = 10)

_ = sns.histplot(data_imputed, x = 'slope', ax = axs[0,2], bins = 10)

_ = sns.histplot(data_imputed, x = 'ca', ax = axs[1,0], bins = 10)

_ = sns.histplot(data_imputed, x = 'thal', ax = axs[1,1], bins = 10)

_ = sns.histplot(data_imputed, x = 'target', ax = axs[1,2], bins = 10)

fig.tight_layout()
plt.savefig(f"histogram_of_numerical_features_pre_transform.jpg")

transformed_data, best_lambda = stats.boxcox(3 + data_imputed['oldpeak'])
data_imputed['oldpeak'] = transformed_data

norm_columns= ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
data_imputed[norm_columns] = stats.zscore(data_imputed[norm_columns])

fig,axs = plt.subplots(2,3,figsize=(16,8))
_ = sns.histplot(data_imputed, x = 'age', ax = axs[0,0], bins = 10)

_ = sns.histplot(data_imputed, x = 'trestbps', ax = axs[0,1], bins = 10)

_ = sns.histplot(data_imputed, x = 'chol', ax = axs[0,2], bins = 10)

_ = sns.histplot(data_imputed, x = 'thalach', ax = axs[1,0], bins = 10)

_ = sns.histplot(data_imputed, x = 'oldpeak', ax = axs[1,1], bins = 10)

fig.tight_layout()
plt.savefig(f"histogram_of_numerical_features_post_transform.jpg")

# Part 7  
fig,axs = plt.subplots(2,3,figsize=(12,6))
_ = sns.scatterplot(data_imputed, x = 'age', y = 'target', ax = axs[0,0])

_ = sns.scatterplot(data_imputed, x = 'trestbps', y = 'target', ax = axs[0,1])

_ = sns.scatterplot(data_imputed, x = 'chol', y = 'target', ax = axs[0,2])

_ = sns.scatterplot(data_imputed, x = 'thalach', y = 'target', ax = axs[1,0])

_ = sns.scatterplot(data_imputed, x = 'oldpeak', y = 'target', ax = axs[1,1])

fig.tight_layout()
plt.savefig(f"scatterplot_of_numerical features_versus_target.jpg")

fig,axs = plt.subplots(2,3,figsize=(12,6))
_ = sns.boxplot(data_imputed, y = 'age', ax = axs[0,0], width = 0.5)

_ = sns.boxplot(data_imputed, y = 'trestbps', ax = axs[0,1], width = 0.5)

_ = sns.boxplot(data_imputed, y = 'chol', ax = axs[0,2], width = 0.5)

_ = sns.boxplot(data_imputed, y = 'thalach', ax = axs[1,0], width = 0.5)

_ = sns.boxplot(data_imputed, y = 'oldpeak', ax = axs[1,1], width = 0.5)

fig.tight_layout()
plt.savefig(f"final_boxplot_of_numerical features.jpg")

# Part 8
data_imputed.to_sql('cleaned_heart', db, if_exists='replace', index= False)
cleaned_data = pd.read_sql_query('SELECT * FROM cleaned_heart', con = db)
cleaned_data.to_csv("cleaned_heart_data.csv")