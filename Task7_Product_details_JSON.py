import json

# Load JSON data from file
with open("products.json", "r") as file:
    products = json.load(file)

#printing the headers
print("\n{:<15}{:<15}{:<15} \n".format("Name", "Price", "Quantity"))
print("-" * 35)

#printing the product deatils from the file.
for product in products:
    print(f"{product['name']:<15} {product['price']:<10} {product['quantity']:<10}")