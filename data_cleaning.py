import pandas as pd

# Step 1: Load CSV (use correct encoding for special characters)
df = pd.read_csv("sales_data.csv", encoding="ISO-8859-1")

# Step 2: Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Step 3: Drop columns with heavy missing data
columns_to_drop = ['ADDRESSLINE2', 'STATE', 'POSTALCODE', 'TERRITORY']
df_cleaned = df.drop(columns=columns_to_drop)

# Step 4: Create a 'YearMonth' column for monthly aggregation
df_cleaned['YearMonth'] = df_cleaned['ORDERDATE'].dt.to_period('M')

# Step 5: Drop duplicate rows (if any)
df_cleaned = df_cleaned.drop_duplicates()

# Optional: Save the cleaned dataset
df_cleaned.to_csv("cleaned_sales_data.csv", index=False)

# Show sample

print(df_cleaned.isnull().sum())


