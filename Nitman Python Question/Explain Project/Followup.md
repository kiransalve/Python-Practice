Why did you choose ARIMA and XGBoost?

Answer:
“I used ARIMA to capture time-series patterns like trend and seasonality. 
XGBoost was used to handle complex and non-linear relationships using features like lag and rolling statistics. 
Comparing both helped improve prediction accuracy.”

How did you handle missing values?

Answer:
“I first analyzed missing data patterns. For time-series data, I used forward fill and interpolation. 
For numerical values, I used mean/median, and for categorical data, mode. 
In cases where missing meant no sales, I replaced it with zero.”

What features did you create?

Answer:
“I created time-based features like month and day, lag features such as previous sales, and rolling statistics to capture trends. 
I also added growth features and encoded categorical variables like product name.”

How did you evaluate the model?

Answer:
“I used a time-based train-test split and evaluated models using MAE, RMSE, and MAPE. 
I also compared ARIMA and XGBoost on the same dataset and validated results using actual vs predicted plots.”


What challenges did you face?

Answer:
“I faced challenges like missing data, unstructured time-series format, and model selection. 
I handled them using proper preprocessing, feature engineering, and comparing models using evaluation metrics.”

How can this be deployed in real-time?

Answer:
“I would deploy the model using an API built with Flask or FastAPI. 
The model would be hosted on Azure cloud, where real-time data is passed to generate predictions. 
Results can be shown using dashboards like Power BI.”


