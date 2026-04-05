while True:
    print("\n=====Calculator=====")
    print("Enter 1 for additon")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for  modulus")
    print("Enter 6 for exit")
    choice = input("Enter your choice:")
    if choice == "6":
        print("Exiting calculator")
        break
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("please enter valid option")
        continue
    try:
        a = float(input("Enter first number:"))
        b = float(input("Enter second number:"))
    except ValueError:
        print("please Enter valid numbers")
        continue
    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    elif choice == "5":
        print("Result:", a % b)
