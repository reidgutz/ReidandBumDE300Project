# ReidandBumJoonDE300Project

To connect to postgres and create the database, first connect to a machine with postgres installed and run the following from the command line:
bash run.sh. This will run the bash files postgres.sh and the files that create the database we will be using.

To complete the exploratory data tasks use the following command from the command line:
python3 proj.py

Algorithms and Reasoning for proj.py

Data Imputation

- For data imputation a variety of methods were used. For certain columns that were missing few values and were approximately normally distributed, we used mean imputation to replace the missing values with the mean of the data. These columns included the columns trestbps and thalach. For other columns we replaced the missing values with the mode of the data since they were categorical and only missing a few values. An example of this is the column restecg.
- For the majority of the columns we used KNN with n = 3. In this method, the missing values are replaced with the value associated with the row's nearest neighbors. This method is useful since it allows for us to deal with a large amount of missing values and replaces the missing value with a value that similar cases would see. This is better than mean imputation since there are a larger amount of missing values and the replaced values are better customized to the data points. 


Outliers

- To deal with outliers we plotted boxplots and used the 1.5 * IQR method. However, since we were measuring potential heart disease we ended up keeping the values that exceeded the upper bound since they could be strong evidence of an unhealthy heart. However, we often removed values that were significantly too low to be normal. For example, resting heart rate and cholesterol being 0 did not seem to make sense as these values we did not view to be possible. Therefore, we dropped those low values. For the trestbps we ended up using 2 * IQR to keep some values we viewed as being significant even though they were below the original 1.5 * IQR threshold.

Analyzing Statistical Measures

- To analyze the statistical measures of our numerical values we generated five number summaries as well as skew and kurtosis.
- For the variable age we found
- For the variable trestbps we found
- For the variable chol we found
- For the variable thalach we found
- For the variable oldpeak we found

Data transformation

- When we plotted the data we found that most of the numerical features were already approximately normally distributed and did not need to be made normal. The only column that was significantly not normal was the column old peak
