import os
import pandas as pd
import json


input_file = "input/data.csv"
data = pd.read_csv(input_file)


output_folder = "output_data"
if os.path.exists(output_folder):
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        os.remove(file_path)
else:
    os.mkdir(output_folder)


categories = {
    "slow_cars": (0, 120),
    "fast_cars": (120, 180),
    "sport_cars": (180, float('inf')),
}


for category, (min_hp, max_hp) in categories.items():
    filtered_data = data[(data['hp'] >= min_hp) & (data['hp'] < max_hp)]
    category_file = os.path.join(output_folder, f"{category}.json")
    filtered_data.to_json(category_file, orient="records", indent=4)


brands = data['brand'].unique()
for brand in brands:
    brand_data = data[data['brand'] == brand]
    brand_file = os.path.join(output_folder, f"{brand}.json")
    brand_data.to_json(brand_file, orient="records", indent=4)
