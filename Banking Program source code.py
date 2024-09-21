title = " Welcome to Python Banking Program"
width = 110
line_width=50

print("*" * width )
print(title.center(width))
print("*" * width)

def show_balance():
    print(f"\n      Your Bank Balance is ₹{float(balance)}")

def deposit() :
    amount = float(input("Enter amount to be deposited : ₹"))
    if amount<0 :
        print("\n  That's not a valid amount")
        return 0
    elif True:
        print(f"\n      Rs.{amount} credited to your bank account")
        return amount
    else:
        return amount

def withdraw() :
    amount = float(input("Enter amount to Withdraw : ₹"))
    if amount > balance :
        print("\n  Insufficient Funds")
        return 0
    elif amount < 0 :
        print("\n  Amount cannot be less than 0)")
        return 0
    elif True :
        print(f"\n      Rs.{amount} debited from your bank account")
        return amount
    else:
        return amount

balance = 100
is_running = True

while is_running:
    print()
    print("_"*line_width)
    print("Banking Program".center(line_width))
    print("_"*line_width)
    print("1-Check Balance")
    print("2-Deposit")
    print("3-Withdraw")
    print("4-Exit")

    choice = input("Enter Choices (1 , 2 , 3 , 4) : ")

    if choice=="1" :
        show_balance()

    elif choice=="2" :
        balance+=deposit()

    elif choice=="3" :
        balance-=withdraw()

    elif choice=="4" :
        is_running = False

    else :
        print("\n  Invalid Choice!")

print("\nThank You! \nHave a Nice day ^_^")
print("~"*line_width)
