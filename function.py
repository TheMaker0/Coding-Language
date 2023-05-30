print()
print("          |     Calculator        |      ")
print("_____________________________________")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

def add(num1, num2):
    com = num1 + num2
    return com 

def diff(num1, num2):
    com = num1 - num2
    return com 

def product(num1, num2):
    com = num1 * num2
    return com  

def quotient(num1, num2):
    com = num1 / num2
    return com 


print("_____________________________________")
print()
print("        |       RESULT        |          ")
print("_____________________________________")
print("Sum is : ", add(num1, num2))
print("Diff is :", diff(num1, num2))
print("Product is :", product(num1, num2))
print("Quotient is :", quotient(num1, num2))




