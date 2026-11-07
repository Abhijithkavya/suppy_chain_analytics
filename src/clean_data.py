import pandas as pd

# Load deliveries dataset
data = pd.read_csv("data/deliveries.csv")

# Check missing values
print("Missing Values:")
print(data.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(data.duplicated().sum())

# Convert date columns
data['expected_delivery_date'] = pd.to_datetime(
    data['expected_delivery_date']
)

data['actual_delivery_date'] = pd.to_datetime(
    data['actual_delivery_date']
)

# Check data types
print("\nData Types:")
print(data.dtypes)

print("\nData Cleaning Completed!")