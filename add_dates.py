import pandas as pd
import random
from datetime import datetime, timedelta

# Load your CSV
df = pd.read_csv('data.csv')

# Generate random dates within a range
start_date = datetime(2024, 1, 1)
df['Date'] = [start_date + timedelta(days=random.randint(0, 90)) for _ in range(len(df))]

# Save back to the same CSV
df.to_csv('data.csv', index=False)

print("✅ Date column added successfully!")
