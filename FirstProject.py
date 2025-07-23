print ("I will become AI Engineer")

import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum of 'Values'
grouped = df.groupby('Category')['Values'].sum()

print(grouped)
