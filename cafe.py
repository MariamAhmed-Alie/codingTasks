# List
menu = ['Coffee', 'Tea', 'Croissant', 'Panini']

# Dictionary 1
stock = { 'Coffee': 50,
         'Tea': 60,
         'Croissant': 90,
         'Panini': 75
         }

# Dictionary 2
price = {'Coffee': 2.50,
         'Tea': 1.75,
         'Croissant': 4.50,
         'Panini': 5.00
         }

# Empty variable
total_stock = 0

# Loop through items and calculate total cost
for item in menu:
    stock_value = stock[item]
    price_value = price[item]
    item_value = stock_value * price_value
    total_stock += item_value

print(f"The total stock value is: £{total_stock}")