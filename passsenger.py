def ordinary():
    try:
        amount = int(input("Amount to pay: "))
        pamasahe = 40
        discount_percent = 0
        discount = amount - pamasahe + discount_percent
        print(f"Discount: {discount_percent}")
        print(f"Change: {discount}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Payment successful.")
    finally:
        print("Thank you for riding with us.\n")


def student():
    try:
        amount = int(input("Amount to pay: "))
        pamasahe = 40
        discount_percent = 20
        discount = amount - pamasahe + discount_percent
        print(f"Discount: {discount_percent}")
        print(f"Change: {discount}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Payment successful.")
    finally:
        print("Thank you for riding with us.\n")


def senior_citizen():
    try:
        amount = int(input("Amount to pay: "))
        pamasahe = 40
        discount_percent = 30
        discount = amount - pamasahe + discount_percent
        print(f"Discount: {discount_percent}")
        print(f"Change: {discount}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Payment successful.")
    finally:
        print("Thank you for riding with us.\n")


print("\n      ----3 TYPES OF PASSENGER----           ")
print("\n1. ORDINARY \n2. STUDENT \n3. SENIOR CITIZEN \n")

choice = int(input("\nEnter your choice : "))

if choice == 1:
    ordinary()
elif choice == 2:
    student()
elif choice == 3:
    senior_citizen()
else:
    print("Invalid choice!")
