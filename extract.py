# Extracting data from Kaggle using kagglehub

import shutil
import kagglehub
import os

# Download the latest version of the dataset
path = kagglehub.dataset_download("karkavelrajaj/amazon-sales-dataset")
print("Path to dataset files:", path)

# Build the source path of the CSV file inside the downloaded dataset
src = os.path.join(path, "amazon.csv")

# Define the destination path (inside your Linux environment for Airflow)
dst_dir = "/home/idrissa/airflow/data"
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, "amazon.csv")

# Copy the file from the Kaggle cache to the destination folder
shutil.copy(src, dst)

print("File copied to:", dst)
