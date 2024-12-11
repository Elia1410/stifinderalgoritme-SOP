# Sample dictionary
data = {
    'a': {'val1': False, 'val2': 1},
    'b': {'val1': True, 'val2': 2},
    'c': {'val1': True, 'val2': 3}
}

# Find the key with the highest 'val2'
dataFiltered = [item for item in data.items() if item[1]['val1']]

max_key = min(dataFiltered, key=lambda item: item[1]['val2'])[0]

# Get the corresponding item
#max_item = data[max_key]

print(f"Key with the highest 'val2': {max_key}")
#print(f"Corresponding dictionary: {max_item}")
