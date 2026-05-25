shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

det_name = input("введи назв. детали ")

det_price = 0
det_count = 0

for name, price in shop:
    if name == det_name:
        det_count += 1
        det_price += price

print(f'стоимость деталей - {det_price}')
print(f'к-во деталей - {det_count}')