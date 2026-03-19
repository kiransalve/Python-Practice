My company is manufacturer of animal feed supplements, so in factory there are issue that they don't know how much production they have to make.

Normaly sales team give forecast in excel sheet based on average of last 3 months , last year same 3 months and last 9 months sales 

but many time forecast and demand not matched and if sales team give low forecast and actual order puched are high and factory can't have stock that much so we loss the customer order.

and if sales team give high forecast and actual order puched are low then that stock lie inside factory 

So my goal is to make model that can predict next month sales qty so that we can reduce the overstocking and understocking scenario

I need sales data of each products for atleast last 5 years, so that I can identify the trends of each products.

so I take data from SAP Hana and store it into MySQL database. I have use python sqlalchemy and hdbcli to extraction and storing sales register to database

then i done data cleaning and data formating in pandas. 

at begining I take 3 columns from sales register - Date, Product and Qty

then check if there is any missing values are there in these three columns, for demand forecasting any of value is null then we need to remove that row to maintain accuracy.

then I collected data like holidays, festivals, promotions, price change.

then I analyse the trend, seasonality, stationarity.

I have done feature engineering like lag feature, rolling average, date features like day, month, weekday-weekend, holiday flags

after cleaning data I have train data on ML models like Linear Regression , XG Boost, ARIMA etc. 
before training I have splited data till last 3 months so I can test the data on this 3 month 

After training I evaluate the model using MAE, RMSE, MAPE.

I compare the XGBOOST and ARIMA, for some product XGBoost perform very well so I have use hybrid aproach by combining both 

ARIMA perform good to capture time based patterns like seasonality and trend

and XG Boost capture comlex and non-linear relationship in the data 
I use flask to deploy model on our AZURE cloud.

