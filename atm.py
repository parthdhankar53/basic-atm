# Simple ATM program

pin = "1234"
balance = 5000

print("Welcome to the ATM")

entered_pin = input("Enter your pin: ")

if entered_pin == pin:
    print("Login successful")

    while True:
        print(" ")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount
            print("Money deposited successfully")
            print("Your new balance is", balance)

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance")
            else:
                balance = balance - amount
                print("Money withdrawn successfully")
                print("Your new balance is", balance)

        elif choice == "4":
            print("Thank you for using the ATM")
            break

        else:
            print("Wrong choice, try again")

else:
    print("Wrong pin, card blocked")
