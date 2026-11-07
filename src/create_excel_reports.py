import pandas as pd
import os

# Create output folder
os.makedirs("outputs/reports", exist_ok=True)

# Load datasets
orders = pd.read_csv("data/orders.csv", sep=";")
products = pd.read_csv("data/products.csv")
inventory = pd.read_csv("data/inventory.csv")

# Revenue calculation
data = pd.merge(orders, products, on="product_id")

data["revenue"] = data["quantity"] * data["unit_price"]

# Total revenue
total_revenue = data["revenue"].sum()

# Top 5 products
top_products = (
    data.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

# Monthly revenue
data["order_date"] = pd.to_datetime(
    data["order_date"], errors="coerce"
)

monthly_revenue = (
    data.dropna(subset=["order_date"])
    .set_index("order_date")
    .resample("ME")["revenue"]
    .sum()
    .reset_index()
)

# Inventory analysis
inventory["available_stock"] = (
    inventory["quantity_on_hand"]
    - inventory["quantity_reserved"]
)

# Low stock products
low_stock = inventory[
    inventory["available_stock"] <= inventory["safety_stock"]
]

# Export to Excel
with pd.ExcelWriter(
    "outputs/reports/supply_chain_report.xlsx"
) as writer:

    data.to_excel(
        writer, sheet_name="Sales Data", index=False
    )

    top_products.to_excel(
        writer, sheet_name="Top Products", index=False
    )

    monthly_revenue.to_excel(
        writer, sheet_name="Monthly Revenue", index=False
    )

    inventory.to_excel(
        writer, sheet_name="Inventory", index=False
    )

    low_stock.to_excel(
        writer, sheet_name="Low Stock", index=False
    )

print("Excel Report Created Successfully!")
print("Total Revenue:", total_revenue)