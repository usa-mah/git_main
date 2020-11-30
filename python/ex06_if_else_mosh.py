'''
Write a program to take 'Weight' as user input and the 'unit' of the weight - either in Kg or Lbs.
Then return the weight in
'''

input_weight = float(input("Please enter your weight in K(g) or L(bs)"))
unit = input("Is that weight in K(g) or L(bs)? Please enter L or K: ")

if unit.upper() == 'L':
    output_weight = input_weight * 0.45
    print(f"Your weight in Kg is {output_weight} ")
else:
    output_weight = input_weight / 0.45
    print(f"Your weight in Lbs is {output_weight}")
