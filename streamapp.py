import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv("cleaned_sales_data.csv")
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df['YearMonth'] = df['ORDERDATE'].dt.to_period('M').astype(str)

# Sidebar filters
st.sidebar.header("Filter Sales Data")
years = df['YEAR_ID'].unique()
months = df['MONTH_ID'].unique()
product_lines = df['PRODUCTLINE'].unique()

selected_year = st.sidebar.selectbox("Select Year", sorted(years))
selected_month = st.sidebar.selectbox("Select Month", sorted(months))
selected_product = st.sidebar.multiselect("Select Product Line", product_lines, default=list(product_lines))

# Apply filters
filtered_df = df[
    (df['YEAR_ID'] == selected_year) &
    (df['MONTH_ID'] == selected_month) &
    (df['PRODUCTLINE'].isin(selected_product))
]

# KPIs
total_sales = filtered_df['SALES'].sum()
total_orders = filtered_df['ORDERNUMBER'].nunique()

st.title("📊 Sales Dashboard")
st.markdown(f"### Year: {selected_year} | Month: {selected_month}")

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("🛒 Total Orders", f"{total_orders}")

# Monthly Sales Trend (Full data)
monthly_sales = df.groupby("YearMonth")['SALES'].sum().reset_index()
fig = px.line(monthly_sales, x="YearMonth", y="SALES", title="Monthly Sales Trend", markers=True)
fig.update_layout(xaxis_title="Year-Month", yaxis_title="Total Sales", title_x=0.5)

st.plotly_chart(fig, use_container_width=True)

from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

st.subheader("🔮 Sales Forecast (Next 6 Months)")

# Prepare monthly sales data
ts_data = df.groupby("YearMonth")['SALES'].sum().reset_index()
ts_data['YearMonth'] = pd.to_datetime(ts_data['YearMonth'])

# Train model
model = ExponentialSmoothing(ts_data['SALES'], trend="add", seasonal="add", seasonal_periods=12)
model_fit = model.fit()

# Forecast next 6 months
forecast_steps = 6
forecast = model_fit.forecast(forecast_steps)

# Combine actual + forecast
forecast_index = pd.date_range(start=ts_data['YearMonth'].max() + pd.DateOffset(months=1), periods=forecast_steps, freq='MS')
forecast_df = pd.DataFrame({'YearMonth': forecast_index, 'SALES': forecast.values})

combined = pd.concat([ts_data[['YearMonth', 'SALES']], forecast_df])

# Plot
fig2, ax = plt.subplots(figsize=(10, 4))
ax.plot(ts_data['YearMonth'], ts_data['SALES'], label='Actual Sales')
ax.plot(forecast_df['YearMonth'], forecast_df['SALES'], label='Forecasted Sales', linestyle='--')
ax.set_title("Sales Forecast (6 Months Ahead)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.legend()

st.pyplot(fig2)
