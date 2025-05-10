# ============== create account =====================================================
import random

def create_account():
    account_num = random.randint(1,100) 
    
    name = input("enter your name: ")
    password = input("enter your password: ")
    balance = int(input("enter your balance: "))

    f=open("accounts.txt", "a")
    f.write(f"{account_num},{name},{password},{balance}\n")
    
    f=open("user_name.txt", "a")
    f.write(f"{name}\n")
    
    f=open("account_num.txt", "a")
    f.write(f"{account_num},{name}\n")
    
    f=open("accounts.txt", "a")
    f.write(f"{password},\n")

    print(f"acount_num is {account_num} your account saved succsesfully!😎")
# ================ create dictionary ==================================================
def load_accounts():
    accounts = {}
    try:
        f= open("accounts.txt", "r")
        for line in f:
            parts = line.strip().split(",")
               
            if len(parts) == 4:
                account_num, name, password, balance = parts
                accounts[name] = {"password": password, "balance": int(balance)}
               
            else:
                print("Skipping malformed line:", line.strip())
    except :
        print("Accounts file not found!")
    return accounts
# ================== save updates ======================================================
def save_new_updates(accounts):
    f=open("accounts.txt", "w")
    for name, data in accounts.items():
            f.write(f"{name},{data['password']},{data['balance']}\n")
# ================== withdraw ===========================================================
def withdraw(accounts, user_name):
    amount = int(input("Enter your withdraw amount: "))

    if amount <= accounts[user_name]["balance"]:
        accounts[user_name]["balance"] -= amount
        print("withdraw successful🤑!")
        print("Your new balance is:", accounts[user_name]["balance"])
        save_new_updates(accounts)

        f=open("tran_history.txt", "a")
        f.write(f"withdraw/{accounts[user_name]["balance"]}/withdraw amount is : {amount}\n")

    else:
        print(" Please check the amount.🤦‍♂️")
#=================== history ==============================================================
def history():
    f=open("tran_history.txt")
    danu=f.read()
    print(danu)
# =================== deposit ==============================================================
def deposit(accounts, user_name):
    amount = int(input("Enter your deposit amount: "))

    if amount > 0:
        accounts[user_name]["balance"] += amount
        print("Deposit successful!")
        print("Your new balance is💸:", accounts[user_name]["balance"])
        save_new_updates(accounts)

        f=open("tran_history.txt", "a")
        f.write(f"deposit/{accounts[user_name]["balance"]}/deposit amount is : {amount}\n")
    
    else:
        print("Invalid deposit amount!😢")
# =================== main code for app =====================================================
print("======(❁´◡`❁) Welcome to Banking (❁´◡`❁)======")
print("Create account: select 1 :")
print("login account: select 2:")
start = input(":")

if start == "1":
   create_account()

elif start == "2":
    accounts = load_accounts()
    print("(((φ(◎ロ◎;)φ)))")
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_name in accounts and accounts[user_name]["password"] == password:
        print("Login successful!😎")
        while True:
            print("==( *︾▽︾)==Select an option==( *︾▽︾)==\n"
                       "Check Balance😊 (c)\n"
                       "\n"
                       "Withdraw Money 🤑(w)\n"
                       "\n"
                       "Deposit Money💸 (d)\n"
                       "\n"
                       "trancection history🤖 (t)\n"
                       "\n"
                       "Exit 👋(e): ")
            option=input(":")
            
            if option == "c":
                print("Your balance is😊:", accounts[user_name]["balance"])
            
            elif option == "w":
                withdraw(accounts, user_name)
            
            elif option == "d":
                deposit(accounts, user_name)
            
            elif option == "t":
                history()
            
            elif option == "e":
                print("Thank you for use banking!👋")
                break
            
            else:
                print("Invalid option. Please try again🥴.")
    else:
        print("Invalid username or password!🤬")
else:
    print("Please select a correct option!🙄")