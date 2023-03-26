import codecademylib3
import pandas as pd
# Load data from csv file
inventory = pd.read_csv('inventory.csv')
# Inspect first 10 rows
print(inventory.head(10))
# Save Staten Island to new dataframe
staten_island = inventory.head(10)
print(staten_island)
# Show available products from Staten Island
product_request = staten_island.product_description
print(product_request)
# Show available seeds at Brooklyn location
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)
# Add in stock column to inventory
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0  else False, axis=1)
# Evaluate the total value of current inventory
inventory['total_value'] = inventory.apply(lambda row: row.price* row.quantity, axis =1)
# Description of each product
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
# Add description to inventory dataframe
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
# Inventory dataframe
print(inventory)
