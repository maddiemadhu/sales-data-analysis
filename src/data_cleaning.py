import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
RAW_DATA_PATH = Path("data/raw/sales_data_sample.xlsx")
CLEAN_DATA_PATH = Path("data/clean/sales_cleaned_data.xlsx")

# -----------------------------
# Load raw data
# -----------------------------
df = pd.read_excel(RAW_DATA_PATH)

print("Raw data loaded")
print(df.info())

# -----------------------------
# Standardize column names
# -----------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# -----------------------------
# Handle missing values
# -----------------------------
# Replace missing STATE values
if "state" in df.columns:
    df["state"] = df["state"].fillna("unknown")

# Replace missing postal code values
if "postalcode" in df.columns:
    df["postalcode"] = df["postalcode"].fillna("unknown")
elif "postal_code" in df.columns:
    df["postal_code"] = df["postal_code"].fillna("unknown")

# -----------------------------
# Data validation checks
# -----------------------------
print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nRow count:", len(df))

# -----------------------------
# Save cleaned data
# -----------------------------
df.to_excel(CLEAN_DATA_PATH, index=False)

print(f"\nCleaned data saved to: {CLEAN_DATA_PATH}")
