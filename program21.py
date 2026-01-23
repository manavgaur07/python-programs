def get_net_price(price, tax_rate=0.07, discount=0.05):
    discounted_price = price * (1-discount)
    net_price= discounted_price * (1 + tax_rate)
    return net_price
net_price = get_net_price(
    100,
    tax_rate= 0.08,
    discount=0.06
) 
print(f'{net_price: .2f}')