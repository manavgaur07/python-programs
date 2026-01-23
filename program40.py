def add(x, y, *args, z):
    return x+y + sum(args) + z
result= add(10, 20, 30, 40, z=50)
print(result)