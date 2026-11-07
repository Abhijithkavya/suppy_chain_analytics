import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV files
orders = pd.read_csv("data/orders.csv", sep=";")
products = pd.read_csv("data/products.csv")

# Step 2: Clean column names
orders.columns = orders.columns.str.strip().str.lower()
products.columns = products.columns.str.strip().str.lower()

# Step 3: Display columns
print("Orders columns:", orders.columns.tolist())
print("Products columns:", products.columns.tolist())

# Step 4: Convert numeric columns
orders["quantity"] = pd.to_numeric(orders["quantity"])
products["unit_price"] = pd.to_numeric(products["unit_price"])

# Step 5: Merge datasets
data = pd.merge(orders, products, on="product_id")

# Step 6: Calculate revenue
data["revenue"] = data["quantity"] * data["unit_price"]

print("\nTotal Revenue:", data["revenue"].sum())

# Step 7: Top 5 products
top_products = (
    data.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products:")
print(top_products)

# Step 8: Top 5 products bar chart
top_products.plot(
    kind="bar",
    title="Top 5 Products by Revenue"
)

plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Step 9: Monthly revenue
data["order_date"] = pd.to_datetime(
    data["order_date"], errors="coerce"
)

monthly_revenue = (
    data.dropna(subset=["order_date"])
    .set_index("order_date")
    .resample("ME")["revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)

# Step 10: Monthly revenue line chart
monthly_revenue.plot(
    kind="line",
    marker="o",
    title="Monthly Revenue Analysis"
)

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()