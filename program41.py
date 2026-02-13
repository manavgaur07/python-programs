print(" 1.add\n 2.difference\n 3.product\n 4.quotient\n 5.remainder\n")
n = int(input("What do you want to want to proceed with"))
if n == 1: 
   num1 = int(input("Enter the number you want to add:"))
   num2 = int(input("Enter other number:"))
   sum = num1+num2
   print(sum)
elif n==2:
   num1 = int(input("Enter first number"))
   num2 = int(input("Enter second number"))   
   diff = num1-num2
   print("here is the diff", diff)
elif n==3:
   num1 = int(input("Enter first number"))
   num2 = int(input("Enter second number"))
   product = num1*num2
   print(product)
elif n==4:
   num1 = int(input("Enter first number"))
   num2 = int(input("Enter second number"))
   quotient = num1/num2
   print(quotient)
elif n==5:
   num1 = int(input("Enter first number"))
   num2 = int(input("Enter second number"))
   remainder = num1%num2
   print(remainder)

