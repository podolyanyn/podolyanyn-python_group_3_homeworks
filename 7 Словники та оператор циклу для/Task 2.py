stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15 }

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3 }

new_dict=dict()

for name , quantity in stock.items():
    for name2,  price in prices.items():
        if name2==name:
            new_dict.update({ name: price*quantity})
print(new_dict)

