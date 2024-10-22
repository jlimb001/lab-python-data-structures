product = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}

print("\nPlease enter the quantity of the following products :")

for item in product:
    quantity = input(f"{item}: ")
    inventory[item] = int(quantity)

#Below codes are for the item that user want to buy
customer_orders = set()

print("\nPlease provide us the 3 items that you like to order from our inventory")

while len(customer_orders) < 3:
  order = input("Order: ").lower()
  if order in product:
     customer_orders.add(order)
  else:
    print("This item is not available")
print(customer_orders)

    
#Following code will show the ordered item and show the remaining item in percentage

#Total number of ordered list
ordered_list = len(customer_orders)
print(f'\nTotal Product Ordered: {ordered_list}')

#Total products in inventory
total_products = sum(inventory.values()) #used inventory.values to access the values
print(f'\nTotal Products: {total_products}')

percentage = (ordered_list / total_products) * 100 #using the formula to get value in percentage
print(f'\nPercentage of Products ordered: {percentage }%')

#Created an variable to update the list in a tuple
order_status = (ordered_list, percentage)
print(f'\nOrder Statistics: \nTotal Products Ordered: {order_status[0]} \nPercentage of Products Ordered: {order_status[1]}% ')


#Updating the inventory by subtracting 1 from the quantity of each product

for items in customer_orders: #going through the customer order to get the updated inventory 
   inventory[item] -= 1

print("\nUpdated inventory:")

for item, quantity in inventory.items():
  print(f"{item}: {quantity}") 