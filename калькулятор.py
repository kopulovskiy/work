def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multyply (x, y):
    return x * y 
def divide (x, y):
    if y != 0:
        return x / y
    else :
        return "error"
    
def calculator():
    print ("simple calculator")
    print ("make ur choise")
    print ("add")
    print ("subtract")
    print ("multiply")
    print ("divide")
    choise = input ("choise operation (1/2/3/4): ")

    if choise in ['1', '2', '3', '4']:
        num1 = float(input("input num1"))
        num2 = float(input("input num2"))

        if choise == '1':
            print ("result", add(num1, num2))
        elif choise == '2':
            print ("result:", subtract(num1, num2))
        elif choise == '3':
            print ("result", multyply(num1, num2))
        else:
            print ("result", divide (num1, num2))
      


(calculator)