import pandas as pd
import os

# Dataset folder path
data_path = "data"

# Load all CSV files
datasets = {}

files = [
    "suppliers.csv",
    "products.csv",
    "warehouses.csv",
    "inventory.csv",
    "purchases.csv",
    "orders.csv",
    "stock_movements.csv",
    "shipments.csv",
    "deliveries.csv"
]

for file in files:
    name = file.replace(".csv", "")
    datasets[name] = pd.read_csv(os.path.join(data_path, file))

    print("\nDataset:", name)
    print(datasets[name].head())
    print("Shape:", datasets[name].shape)
    print("Missing values:")
    print(datasets[name].isnull().sum())
    print("-" * 40)