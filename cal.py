while True :

    print("\n1. Exit")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplition")
    print("5. Division")
    print("6. Average")
    print("7. Square")
    print("8. Cube")
    print("9. Remainder")
       
    choice = int(input("Enter choice :" ))

    if choice == 1:
        print("closed")
        break

    elif choice == 2 :
        num1 = float(input("Enter 1st no :"))
        num2 = float(input("Enter 2nd no :"))
        ans = num1 + num2
        print("addition is", ans)

    elif choice == 3 :
        num1 = float(input("Enter 1st no :"))
        num2 = float(input("Enter 2nd no :"))
        ans = num1 - num2
        print("subtraction is", ans)

    elif choice == 4 :
        num1 = float(input("Enter 1st no :"))
        num2 = float(input("Enter 2nd no :"))
        ans = num1 * num2
        print("multipication is", ans)

    elif choice == 5 :
        num1 = float(input("Enter 1st no :"))
        num2 = float(input("Enter 2nd no :"))
        ans = num1 / num2
        print("division is", ans)

    elif choice == 6 :
        num1 = float(input("Enter 1st no :"))
        num2 = float(input("Enter 2nd no:"))
        ans = (num1 + num2) /2
        print("average is", ans)

    elif choice == 7 :
        num1 = float(input("Enter 1st no:"))
        ans = num1 ** 2
        print("square is", ans)

    elif choice == 8:
        num1 = float(input("Enter 1st no :"))
        ans = num1 ** 3
        print("cube is", ans)

    elif choice == 9:
        num1 = float(input("Enter 1st no :"))
        num2 = float(input("Enter 2nd no :"))
        ans = num1 % num2 
        print("remainder is", ans)

    else :
        print("Invalid Input")
        
        