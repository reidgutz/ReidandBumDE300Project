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

- To analyze the statistical measures of our numerical values we generated five number summaries as well as skew, mean and kurtosis.
- For the variable age we found it to be between 28 and 77 with a mean around 52.8 . There appears to be very little skew and kurtosis as both are around 0. This indicated that the variable may be normally distributed.
- For the variable trestbps we found the data to be between 92 and 200 with a mean around 132.6. The skewness and kurtosis measures are both under 1, which indicates that there is not much to be concerned about regarding tail values
- For the variable chol we found the data to be between 69 and 603 with a mean of 247. There is a kurtosis over 4 and skew over 1. This is due to the nature of cholesterol, which can be very high in serious cases of heart disease. Therefore, we would expect a large positive skew and will not remove outliers here. The rest of the data appears to be normally distributed when plotted.
- For the variable thalach we found that the data was between 69 and 202 with a mean of 140.6. There is 
- For the variable oldpeak we found

Data transformation

- When we plotted the data we found that most of the numerical features were already approximately normally distributed and did not need to be made normal. The only column that was significantly not normal was the column old peak. For this column we used a box-cox transformation. The boxcox method works by varying an exponential parameter lambda to find an optimal transformation of the distribution. Using a log transofrmation did not make this more normal so the box-cox method was used as an alternate method.

Box-Plot Analysis

- From the boxplot for age and thalach we see it centered at 0 and it looks to be normally distributed. This makes sense since we z-scored the data.
- From the boxplot for trestbps and chol we see that there are outliers that have been intentionally left in since we viewed them as important and they are also centered at 0 due to z scoring
- From the boxplot for old peak we see that there is not really a lower hinge due to the exponential nature of the distribution - there are many values congregated in the lower region. This is also centered at 0 due to the z-scoring. 

Scatter-Plot Analysis

- old peak looks to have higher number correlating towards target 1. Target 0 seems to be more aggregated towards the middle values
- age, trest, chol look to be pretty evenly dispersed and any differences do not appear to be significant
- Thalach has higher values being more associated with target 0
