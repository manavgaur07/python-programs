x = input('Enter The Year:')
if(int(x)%4==0 and int(x)%100!=0) or (int(x)%400==0):
    print(f"{x} is a leap year")
else:
    print(f"{x} is not a leap year.")
