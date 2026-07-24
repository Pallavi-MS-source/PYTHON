def discount_price(original_price,discount_percent):
    final_price = original_price - (original_price * discount_percent/100)
    print(f"final price is {final_price}")
discount_price(1000,20)
