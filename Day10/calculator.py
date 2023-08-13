import art 

print(art.logo)

#calculate function 

#Add function
def add(a,b):
    return a + b

#subtract function
def subtract(a,b):
    return a - b

#multiply function
def multiply(a,b):
    return a * b

#divide function
def divide(a,b):
    return a / b

#create a dictionary named operations, the key is the symbol we use to do operation, the value is the function itself

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate():
    #ask user for input num1 and num2, also the operations they wnat to do 

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    for key in operations:
        print(key)

    operation_symbol = input("Enter the operation you want to do: ")

    #calculate the answer

    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_cal = input(f'Type y to continue calculating with {answer}, or type n to exit.:')

    while continue_cal.lower() == 'y':
        continue_symbol = input('pick an operation: ')
        continue_num = float(input('what is the next number?: '))
        continue_answer = operations[continue_symbol](answer,continue_num)
        print(f"{answer} {continue_symbol} {continue_num} = {continue_answer}")
        continue_cal = input(f'Type y to continue calculating with {answer}, or type n to exit.:')

    calculate()


calculate()