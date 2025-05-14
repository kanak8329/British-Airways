import pandas as pd

# Load dataset
df = pd.read_csv("customer_booking.csv")

# Basic exploration
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Value counts of target column (e.g., 'booking_complete' or similar)
print(df['booking_complete'].value_counts())  # Replace with actual column name
