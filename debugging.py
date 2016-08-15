import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

days = []

price = INITIAL_PRICE
print("${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    choice = random.randint(1, 2)
    if choice == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
       price_change = random.uniform(-MAX_DECREASE, 0)

    price = (price + price_change)
    days.append(price)
    print("On day ",days.index(price),"${:,.2f}".format(price))