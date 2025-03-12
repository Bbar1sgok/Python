print("""
****************************************************
ATM APPLICATION

WELCOME
TRANSACTIONS;

1-> BALANCE INQUIRY 
2-> DEPOSIT
3-> WITHDRAW MONEY
Press "q" to exit the program
****************************************************
""")

balance = 2000

while True:
    process = input("Please select transaction: ")
    if (process.lower() == "q"):
        print("We wait again")
        break

    elif(process == "1"):
        print(f"Your Account Balance: {balance} ")
        process = input("'1' to take another action, '2' to exit: ")
        if (process == 1):
            pass
        elif(process == "2"):
            break

    elif (process == "2"):
        deposit = float(input("Please enter the fee you want to deposit: "))
        balance += deposit
        print(f"Your transaction was completed successfully.Your new balance {balance}")
        process = input("'1' to take another action, '2' to exit: ")
        if (process == 1):
            pass
        elif (process == "2"):
            break

    elif (process == "3"):
        withdraw_money = float(input("Please enter the money you want to withdraw: "))
        balance -= withdraw_money
        if(balance < 0):
            balance+=withdraw_money
            print(f"insufficient balance.Your balance in the account {balance} ")
            process = input("'1' to take another action, '2' to exit: ")
            if (process == 1):
                pass
            elif (process == "2"):
                break

        elif(balance >= 0):
            print(f"Money has been deducted from your account. Your new balance {balance}")
            process = input("'1' to take another action, '2' to exit: ")
            if (process == 1):
                pass
            elif (process == "2"):
                break
    else:
        print("""
        ****************************************************
        Please press the correct button
        TRANSACTIONS;

        1-> BALANCE INQUIRY 
        2-> DEPOSIT
        3-> WITHDRAW MONEY
        Press "q" to exit the program
        ****************************************************
        """)
