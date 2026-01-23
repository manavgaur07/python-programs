country = [
    ['china', 13922054],
    ['india', 13922089],
    ['russia', 13922985],
    ['england', 13922965],
    ['america', 13922094]
]
populated = filter(lambda c: c[1] > 10000000, country)
print(list(populated))