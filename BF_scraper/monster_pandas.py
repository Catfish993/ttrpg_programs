import pandas as pd
import re

# Load JSON
df = pd.read_json("BF_scraper/monsters_a.json")

# Flatten the nested 'stats' column
flat_df = pd.json_normalize(df.to_dict(orient="records"))

# Filter rows where Hit Dice starts with "1", using regex
pattern = r'^1(\D|$)'  # matches '1', '1 to 4', '1*', '1+1', etc.
oneish_hd = flat_df[flat_df["stats.Hit Dice"].str.contains(pattern, na=False)]

# Select only the relevant columns
filtered = oneish_hd[["name", "stats.Hit Dice"]]

# Save to clean JSON
filtered.to_json("one_hd.json", orient="records", indent=2)

print(f"✅ Saved {len(filtered)} filtered monsters to one_hd.json")