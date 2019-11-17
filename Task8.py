num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num2 >= num1:
    for num1 in range(num1,num2+1):
        print(num1)
else:
    print('Num2 less then num1')

