basket= [
    {'fruit':'apple','qty': 20},
    {'fruit':'banana','qty': 30},
    {'fruit':'orange','qty': 10},
    {'fruit':'papaya','qty': 40}  
]
fruit=input('Enter Name Of Fruit')
index=0
while index < len(basket):
    item = basket[index]
    if item['fruit'] == fruit:
        print(f'The basket has{item["qty"]} {item["fruit"]}(s)')
        found_it=True
        break
    index+=1
else:
    qty= int(input(f"Enter the qty for {fruit}:"))
    basket.append({'fruit':fruit, 'qty': qty})
    print(basket) 

        