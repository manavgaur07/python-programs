from random import randint
MIN=0
MAX=10
secret_number= randint(MIN,MAX)
attempt = 0
input_number= int(input(f"Enter the number between{MIN} and {MAX}"))
attempt+=1
if input_number>secret_number:
    print('Number is smaller')
elif input_number<secret_number:
    print("number is bigger")
else:
    print(f'Bingoo!!{attempt} attempt used')
while input_number!=secret_number:
    input_number= int(input(f"Enter the number between{MIN} and {MAX}"))
    attempt+=1
    if input_number>secret_number:
        print('Number is smaller')
    elif input_number<secret_number:
        print("number is bigger")
else:
    print(f'Bingoo!! {attempt} attempt used')