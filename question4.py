def sacco_trasantions():
  account_balance = 0
run = 1
while run == 1:
  print ("\nWelcome to, WITIAcademy Sacco.") 
# menu
print ("1.Deposit money")
print("2.Withdraw Money")
print("3.Check balance")
student_choice = int(input('Enter your selection(1,2 or 3'))

if student_choice == 1:
  print("\n...processing a deposit amount transaction.... ")
  deposit_amount = int(input('Enter the amount to be deposited:'))

  # check if deposited amount is less than 1000
  if deposit_amount <1000:
    print('\nminimum deposit is 1000')
  else:
   account_balance = deposit_amount
print(f"Dear student you have deposited {deposit_amount:,} and your new account balance is {account_balance}")

if student_choice == 2:
  print ('\n... processing a withdraw...')
withdraw_amount = int(input('Enter the amount to be withdrawn:'))

if account_balance == 0:
  print("Your account balance is 0")
elif withdraw_amount < 500:
  print("\nminimum amount to be writhdrawn is 500")
elif withdraw_amount > account_balance:
  print("withdraw failed due to insufficient funds") 
else: account_balance = withdraw_amount
print (f"Dear student, you have withdraw {withdraw_amount:,} and your new account_balance is {account_balance}")