prices=[100,200,300]

discount=10

final_price=[]

for price in prices:
    calculated_price = price - (price * discount / 100)
    final_price.append(calculated_price)

print(final_price)
