from prog1 import Calculator
option = 0
try:
    input1 = float(input('Enter a number'))
    input2 = float(input('enter a number'))
    c1 = Calculator(input1,input2)
    print('1.add 2.sub 3.mul 4.div')
    option = int(input())
    if(option == 1):
        print(c1.add())
    elif(option == 2):
        print(c1.sub())
    elif(option == 3):
        print(c1.mul())
    else:
        print(c1.div())
except ValueError as ve:
    print("enter float number only")
