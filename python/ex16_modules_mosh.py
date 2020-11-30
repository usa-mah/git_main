import ex16_modules_converter

print(ex16_modules_converter.kg_to_lbs(70))



# another way to import something specific from a module:

from ex16_modules_converter import lbs_to_kg

# but now you will have direct access to the function
print(lbs_to_kg(70))




# Exercise
# --------
# Find the max number from a list

from ex16_modules_converter import find_max

my_list = [10, 3, 6, 2]
max_number = find_max([10, 3, 6, 2, 15, 23, 9, 3])
print(max_number)

        
