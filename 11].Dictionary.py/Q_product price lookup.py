"""
Construct a dictionary containing 4 product names and their price.Prompt
the user to enter name. Use in keyword to check if it exists,if so
display its price.Otherwise inform the user "Product NOt Found".
"""
prdt = {'comb':50,'powder':40,'cream':20,'kajal':30}
product = input("Enter the product name = ")

if product in prdt:
    print(prdt[product])
else:
    print(f" Product Not Found")
