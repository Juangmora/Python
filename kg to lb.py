***
Create a Python program that converts kilograms to pounds.
Use at least 4 different samples to converts.
***
# Variables for kilgram values
kg_val_1 = 58.967 # My weight
kg_val_2 = 7.71107 # My grandsons current weight
kg_val_3 = 72.5748 # Weight of Miles Morales (Spider-man)
kg_val_4 = 1914.613 # Weight of my future car (Acura TLX Type S)

# Conversion factor: 1 pound = 0.453592 kilgrams
conversion_factor = 0.453592

# Convert kilograms to pounds
pounds_1 = kg_val_1 / conversion_factor
pounds_2 = kg_val_2 / conversion_factor
pounds_3 = kg_val_3 / conversion_factor
pounds_4 = kg_val_4 / conversion_factor

# Output the results
print(f"{kg_val_1} kilograms is equal to {pounds_1:.2f} pounds.")
print(f"{kg_val_2} kilograms is equal to {pounds_2:.2f} pounds.")
print(f"{kg_val_3} kilograms is equal to {pounds_3:.2f} pounds.")
print(f"{kg_val_4} kilograms is equal to {pounds_4:.2f} pounds.")
