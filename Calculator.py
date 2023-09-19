def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
for i in operations:
    print(i)
function = input("What function would you like to operate: ")
calculation_function = operations[function]
answer = calculation_function(num1, num2)
print(f"{num1}{function}{num2} = {answer}")