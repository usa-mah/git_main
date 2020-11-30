print('prog01')
house_price = 1000000
good_credit = True

if good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2

print(f'down_payment is {down_payment}')

name = 'Jajabor'
print('\n')
print('prog02')
if len(name) < 3:
    print('The name must have 3 characters')
elif len(name) > 50:
    print('The name must not be greater than 50 characters')
else:
    print('The name looks fantastic')