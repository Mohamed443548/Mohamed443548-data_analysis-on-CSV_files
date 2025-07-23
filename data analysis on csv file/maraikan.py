import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Step 1: Load CSV file
df = pd.read_csv("mohamed.csv")

# Step 2: Preview data
print("🔍 Preview of the data:")
print(df.head())

# Step 3: Total Sales by Product
sales_by_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\n📦 Total Sales by Product:")
print(sales_by_product)

# Step 4: Plot Sales by Product
plt.figure(figsize=(10, 6))
sales_by_product.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Step 5: Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Step 6: Group by Date and sum Sales
sales_by_date = df.groupby('Date')['Sales'].sum()

# Step 7: Plot Sales Over Time
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sales_by_date.plot(kind='line', marker='o', color='orange')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

