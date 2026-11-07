import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load inventory dataset
inventory = pd.read_csv("data/inventory.csv")

# Step 2: Clean column names
inventory.columns = inventory.columns.str.strip().str.lower()

# Step 3: Convert stock columns to numeric
stock_columns = [
    "quantity_on_hand",
    "quantity_reserved",
    "safety_stock"
]

for col in stock_columns:
    inventory[col] = pd.to_numeric(
        inventory[col], errors="coerce"
    ).fillna(0)

# Step 4: Calculate available stock
inventory["available_stock"] = (
    inventory["quantity_on_hand"] -
    inventory["quantity_reserved"]
)

print("\nInventory Details:")
print(inventory.head())

# Step 5: Calculate total stock
print("\nTotal Available Stock:",
      inventory["available_stock"].sum())

# Step 6: Find low-stock products
low_stock = inventory[
    inventory["available_stock"] <= inventory["safety_stock"]
].copy()

print("\nLow Stock Products:")
print(low_stock)

# Step 7: Create chart only if low-stock records exist
if not low_stock.empty:

    low_stock.plot(
        x="product_id",
        y="available_stock",
        kind="bar",
        title="Low Stock Analysis",
        legend=False
    )

    plt.xlabel("Product ID")
    plt.ylabel("Available Stock")
    plt.tight_layout()
    plt.show()

else:
    print("\nNo low-stock products found.")
    print("All products have stock above their safety stock level.")

# Step 8: Display stock chart for all products
inventory.plot(
    x="product_id",
    y="available_stock",
    kind="bar",
    title="Available Inventory Analysis",
    legend=False
)

plt.xlabel("Product ID")
plt.ylabel("Available Stock")
plt.tight_layout()
plt.show()

print("\nInventory Analysis Completed!")