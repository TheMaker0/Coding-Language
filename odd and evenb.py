while True:
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    repeat = input("Do you want to enter another number? (y/n): ")
    if repeat.lower() == 'n':
        break
