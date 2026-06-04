import os
import json

# Gets the exact directory where your script is running
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combines the directory path with your JSON filename
json_path = os.path.join(script_dir, "78420173.json")

# Open and read the match data
with open(json_path, "r") as f:
    match_data = json.load(f)

print("Match data successfully parsed from repository folder!")
