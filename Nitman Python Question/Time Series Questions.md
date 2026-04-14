1. What is Time Series?

Data collected over time (daily, monthly, yearly).

Example: daily sales, stock prices

2. What is Stationarity?

When data behavior is stable over time (mean, variance don’t change).

Why important? Most models (like ARIMA) need stable data.

3. What are components of Time Series?

Trend → long-term increase/decrease

Seasonality → repeated pattern (monthly/weekly)

Noise → random variation

4. What is Differencing?

Subtract previous value from current value to make data stable.

Example: Today sales – Yesterday sales

5. What is ARIMA?

ARIMA = AR + I + MA

AR (Auto Regression) → depends on past values
I (Integrated) → differencing
MA (Moving Avg) → depends on past errors
