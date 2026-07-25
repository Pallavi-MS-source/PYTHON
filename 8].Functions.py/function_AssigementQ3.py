"""
Write a function tax_calculation(income) that takes annual income and 
returns the tax amount based on these slabs
up to 2,50,000 -> no tax
2,50,001 to 5,00,000 -> 5%
5,00,001 to 10,00,000 -> 20%
above 10,00,000 -> 30%
"""
def tax_calculation(income):
    if income <= 250000:
        tax =  0
    elif income <= 500000 :
        tax = income * 0.05
    elif income <= 1000000 :
        tax =  income * 0.2
    else:
        tax = income * 0.3
    return tax
income = int(input("Enter annual income = "))
print("tax = ",tax_calculation(income))
