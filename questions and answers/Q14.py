"""
 A shop gives discount based on purchase amount 
 above 5000 20% discount
 above 2000 10%
 above 1000 5%
 1000 or below no discount
 """
p_amount = int(input(" Enter the bill of customer = "))

if p_amount > 5000:
       payment =  p_amount - p_amount * 0.2

elif p_amount > 2000:
        payment =  p_amount - p_amount * 0.1

elif p_amount > 1000:
        payment =  p_amount -  p_amount * 0.05

else:
      payment = p_amount


print(payment)