#Making the code with comments helpful for reference/understanding

import json

# Let's start with loading the specs from our very own json file
with open('spec.json', 'r') as f:
    spec = json.load(f)

# Now, let's extract the Columns, Offsets, Encoding details from our json file
columns = spec['ColumnNames']                      # Lists out the column names such as f1, f2, f3 etc
offsets = list(map(int, spec['Offsets']))           # Convert strings to integers
encoding = spec.get('FixedWidthEncoding', 'utf-8')      # Encoding purpose as we follow windows-1252

# generating some sample data
data = [
    {"f1": "1", "f2": "Andrew", "f3": "A", "f4": "B", "f5": "andrew@demyst.com", "f6": "USA", "f7": "1234567890", "f8": "Newark", "f9": "Next to New York City", "f10": "Employee"},
    {"f1": "2", "f2": "Tom", "f3": "T", "f4": "M", "f5": "tom@demyst.com", "f6": "MEX", "f7": "0987654321", "f8": "Boston", "f9": "a city in Massachusetts", "f10": "Vendor"}
]

# Let's define a function for making the match as per the required width, like truncating or padding
def pad_or_truncate(text, width):
    return str(text)[:width].ljust(width)

# Now let's generate the fixed-width file
with open('data.fixed', 'w', encoding=encoding) as f:
    if spec.get('IncludeHeader', 'False').lower() == 'true': #including header
        header = ''.join(pad_or_truncate(col, width) for col, width in zip(columns, offsets))
        f.write(header + '\n')  # Let's have a newline after the header

    # next comes, writing the actual data
    for row in data:
        line = ''.join(pad_or_truncate(row.get(col, ''), width) for col, width in zip(columns, offsets))
        f.write(line + '\n') # for newline

# print the results
print("Fixed-width file named 'data.fixed' has been generated")
