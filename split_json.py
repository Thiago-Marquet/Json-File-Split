import json
import os

file_name = "splited" # Specify the base name for split files

# Open and read the source JSON file containing data to split
with open('large_json_file.json', 'r') as f:
    data = json.load(f)

# Calculate the chunk size (x MB in bytes)
max_megabytes = 10
chunk_size = max_megabytes * 1024 * 1024

chunks = []
current_chunk = []
current_size = 0

# Loop through each item in the source data
for item in data:
    item_size = len(json.dumps(item)) # Calculate the size of the JSON-encoded item
    
     # Check if adding the current item would exceed the chunk size
    if current_size + item_size <= chunk_size:
        current_chunk.append(item)
        current_size += item_size
    else:
        chunks.append(current_chunk)
        current_chunk = [item]
        current_size = item_size

if current_chunk:
    chunks.append(current_chunk)

for i, chunk in enumerate(chunks):

    splited_file = f'./split/{file_name}_{i + 1}.json' # Save to a folder called 'split'
    with open(splited_file, 'w') as f:
        json.dump(chunk, f, indent=2)

print(f'Split {len(data)} items into {len(chunks)} chunks.')
