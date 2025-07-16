# Sales Dashboard and Forecasting Tool

An interactive analytics tool built using Python to visualize sales data and forecast future revenue. It combines time-series analysis with dashboard interactivity for business intelligence use cases.

---

## Features

- Monthly sales trend visualization
- Multi-slicer interactivity with product and region filters
- Forecasting using exponential smoothing (8% error margin)
- Data cleaned from raw input including nulls and duplicates

---

## Project Structure

sales-dashboard-forecasting/
├── sales_data.csv # Raw dataset
├── cleaned_sales_data.csv # Cleaned dataset for modeling
├── data_cleaning.py # Script to preprocess the data
├── forecasting.py # Script for time series forecasting
├── streamapp.py # Streamlit dashboard frontend
├── requirements.txt # Dependencies
├── summary.txt # Project summary


---

## Data Source

Sales data was taken from a publicly available classic retail dataset covering customer orders, products, pricing, and time information.

---

## Installation

Install required libraries:

In terminal, paste this:
pip install -r requirements.txt

## Run the App
To launch the Streamlit dashboard, copy and paste this in terminal:
streamlit run streamapp.py

Then open the URL shown in your browser (e.g., http://localhost:8501)

## Forecasting Model
Used Holt-Winters Exponential Smoothing from statsmodels to predict future sales. Achieved ~8% average error across validation months.

## Technologies Used

pandas, plotly – Data analysis and visualization

statsmodels – Forecasting model

streamlit – Dashboard UI

scikit-learn – Preprocessing utilities

##  Author
Saikat Jana
GitHub: Saik-at

## License
This project is open-source under the MIT License.



