# Importing relevant libraries
import numpy as np

# Recipe quantities for cupcakes in cups

cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# Bettys recipes 
# Extract recipes from csv file
recipes = np.genfromtxt('recipes.csv',delimiter=',')
# Display recipes 
print(recipes)

# Number of eggs for each recipe
eggs = recipes[:,2]
# Recipes that use exactly 1 egg
egg = eggs[eggs == 1]

# Cookies recipe quantities
cookies = recipes[2,:]
# Double batch of cupcakes
double_batch = cupcakes*2

# Shopping list for double batch of cupcakes and one batch of cookies
grocery_list = cookies + double_batch

print(grocery_list)
