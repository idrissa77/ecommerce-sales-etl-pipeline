# Purpose: preprocess and clean Amazon dataset

import pandas as pd
import os

input_file = "/home/idrissa/airflow/data/amazon.csv"

output_file = "/home/idrissa/airflow/data/amazon_clean.csv"

df = pd.read_csv(input_file)


# Remove duplicates based on "product_id"
df = df.drop_duplicates(subset="product_id", keep="first")

print(df.isna().sum())

# "rating_count" has 2 missing values. Display their index
missing_rows = df[df["rating_count"].isna()]
print(missing_rows.index.tolist())

# This missings values of "rating_count" column are on line 282, and 324
# Fill the first NaN by 61 (found in amazon via the product's link )
df.at[282, "rating_count"]= 61

# Drop line 324 because the product is not findable on amazon using its link 
df = df.drop(index=324)

# Cleaning and converting numerical data
df["discounted_price"] = df["discounted_price"].replace('[₹,]', '', regex=True).astype(float)
df["actual_price"] = df["actual_price"].replace('[₹,]', '', regex=True).astype(float)
df["discount_percentage"] = df["discount_percentage"].replace('%', '', regex=True).astype(float)
# remove separators then convert to float
df["rating_count"] = df["rating_count"].replace({',': ''}, regex=True).astype(float)
# keep only valid numeric values in'rating' then convert to float
df = df[df["rating"].str.replace(".",'',1).str.isdigit()]
df["rating"] = df["rating"].astype(float)


# Save cleaned file
df.to_csv(output_file, index=False)

print(f"Cleaned dataset saved to: {output_file}")


