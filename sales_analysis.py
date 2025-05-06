import pandas as pd

# Step 1: Load Data with specific encoding
file_path = 'sales_data_sample.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Step 2: Explore Data
print("First 5 rows of the data:")
print(df.head())

# Print the column names to ensure 'SALES' exists
print("\nColumn names in the dataset:")
print(df.columns)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check data types and basic info
print("\nData Info:")
print(df.info())

# Step 3: Data Cleaning (if necessary)
# Check if 'SALES' exists and then drop rows with missing sales data
if 'SALES' in df.columns:
    df = df.dropna(subset=['SALES'])
else:
    print("The 'SALES' column does not exist in the dataset.")

# Step 4: Basic Analysis
# Total Sales
total_sales = df['SALES'].sum() if 'SALES' in df.columns else 0
print(f"\nTotal Sales: ${total_sales:,.2f}")

# Sales by Region
if 'TERRITORY' in df.columns:
    sales_by_region = df.groupby('TERRITORY')['SALES'].sum()
    print("\nSales by Region:")
    print(sales_by_region)

# Most Profitable Products
if 'PRODUCTLINE' in df.columns:
    most_profitable_products = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Profitable Products:")
    print(most_profitable_products)

# Step 5: Sorting and Ranking
# Rank regions by sales (highest to lowest)
if 'TERRITORY' in df.columns:
    sales_by_region_sorted = sales_by_region.sort_values(ascending=False)
    print("\nRegions Ranked by Sales:")
    print(sales_by_region_sorted)

# Rank products by sales (highest to lowest)
if 'PRODUCTLINE' in df.columns:
    most_profitable_products_sorted = most_profitable_products.sort_values(ascending=False)
    print("\nTop 10 Products Ranked by Sales:")
    print(most_profitable_products_sorted)

# Step 6: Save the cleaned data to a new CSV
df.to_csv('cleaned_sales_data.csv', index=False)
