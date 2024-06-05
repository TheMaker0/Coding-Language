import time

def printslow(*args, delay=0.1, sep=' ', end='\n', flush=False):
    for arg in args:
        for char in str(arg):
            print(char, end='', flush=flush)
            time.sleep(delay)
        print(sep, end='', flush=flush)
    print(end=end, flush=flush)

def Calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Calculator Menu: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division ")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        result = num1 + num2
        operation = "addition"
    elif choice == 2:
        result = num1 - num2
        operation = "subtraction"
    elif choice == 3:
        result = num1 * num2
        operation = "multiplication"
    elif choice == 4:
        result = num1 / num2
        operation = "division"
    else:
        print("Invalid choice!")
        exit()
    print("The result of the", operation, "of", num1, "and", num2, "is:", result)

                
def Age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are old!")
    else:
        print("You are young!")

        
def Converter():
    feet = float(input("Enter the measurement in feet: "))
    inches = feet * 12
    print(feet, "feet is equal to", inches, "inches.")

    
def Vowels():
    char = input("Enter a character: ")
    switcher = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
    }
    print(switcher.get(char.lower(), "Not a vowel"))
    
    
def Loop():
    sum = 0
    for i in range(1, 101):
        if i % 5 == 0:
            sum += i
    print("The sum of all numbers divisible by 5 from 1 to 100 is:", sum)




print("      ----WELCOME TO PYTHON----           ")
print("____________________________________________________________")
username = input("\n          Username: ")
password = int(input("          Password: "))
print("____________________________________________________________")

if password == 1234:
    
    print("\n         -Login successful!\n")
    print("____________________________________________________________")
    print("\n         Menu: \n            1. Calculator \n            2. Age \n            3. Converter \n            4. Vowels \n            5. Loop")
    choice = int(input("\n            Enter your choice : " + "\nR"))
    if choice == 1:
        Calculator()
    elif choice == 2:
        Age()
    elif choice == 3:
        Converter()
    elif choice == 4:
        Vowels()
    elif choice == 5:
        Loop()
    elif choice == 6:
        jamaica()
    else:
        print("Invalid choice!")
else:
    print("Incorrect password. Login failed.") 
