'''
In this file, we will be creating a bank account simulator where we will have different features and actions.
**Features**
We will create an account for a person that will consist on name, password, and balance.

Actions:
1. Deposit.
2. Withdraw.
3. Show Balance
4. Show details
5. Exit

'''

def deposit():
  pass

def withdraw():
  pass

def show_balance():
  pass

def show_details():
  pass

def menu():
  print(f"""Welcome to the bank account.
        Please select an option:
        1. Deposit.
        2. Withdraw.
        3. Show balance.
        4. Show details.
        5. Exit""")

def main():

  while True:
    menu()
    option = int(input("Select an option between 1 and 5: "))
    if option == 1:
      print("You chose to deposit")
    elif option == 2:
      print("You chose to withdraw")
    elif option == 3:
      print("You chose to show balance")
    elif option == 4:
      print("You chose to show details")
    elif option == 5:
      print("Bye!")
      break
    else:
      print("That's not a valid option")
      
if __name__ == "__main__":
  main()