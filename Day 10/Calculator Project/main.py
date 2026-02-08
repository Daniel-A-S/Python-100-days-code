from art import logo
print(logo)
print("Welcome to the Python Calculator!\n")

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1*n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

# step2 creating a dictionary
operations={
    "+": add,
    "-" :subtract,
    "*" : multiply,
    "/" :divide
}

def calculator ():
    n1 = int(input("please enter the first number "))
    continue_or_not = True
    while continue_or_not:

        for symbols in operations:
            print(symbols)

        operation_symbol = input("please enter what kind of operation you would like,+,-,*, / ")
        n2 = int(input("please enter the second number "))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(n1,n2)
        if isinstance(answer,str):
            return
        else:
            print(f" the solution to {n1} {operation_symbol} {n2}={answer}")
            continue_response=input("do you like to use the previous result of the calculation, Y or N ").upper()
            if continue_response=="Y":
                n1=answer
            else:
                continue_or_not=False
                print("Thank you for using the calculator!")
calculator()

