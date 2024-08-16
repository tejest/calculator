def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


opertations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}


def calculator():
    should_accumalte=True
    num1=float(input("first number:"))

    while should_accumalte:
        for symbol in opertations:
            print(symbol)

        operation_symbol=input("operation:")
        num2=float(input("second number:"))
        answer=opertations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2}:{answer}")

        choice=input(f"Type 'y' if you want to continue else 'n' to stop")

        if choice=='y':
            num1=answer
        else:
            should_accumalte=False
            print("/n"*20)
            calculator()

calculator()




