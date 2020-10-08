class Bank():
    def __init__(self, account, pin, balance):
        self.account = account
        self.pin = pin
        self.balance = balance
   
    def account_deposit(self, deposit):
        amount_to_deposit = input('How much would you like to deposit today? \n')
        self.balance += int(amount_to_deposit)
        print(f'You deposited ${deposit} into your account, your new balance is ${self.balance}.')

    def account_withdrawal(self, withdrawal):
        amount_to_withdraw = input('How much would you like to withdraw today?')
        self.balance -= int(withdrawal)
        print(f'Your new balance is ${self.balance}.')
    def account_bill_pay(self, company_paid, amount):
        amount_to_pay = input('What amount would you like to pay?')
        self.balance -= int(amount_to_pay)
        print(f'Check issued to {self.company_paid} in the amount of ${self.amount}.\n')
        print(f'Your new balance is ${self.balance}.')
    def account_balance(self):
        print(f'Your balance is ${self.balance}.')

user_one = Bank(123456, 2222, 1500.69)
user_two = Bank(282828, 4567, 480.50)


program_run = True
   


def program_run(self):
        program_run = True
        while program_run == True:
            input('Please enter your pin')
            pin = int(input(self.pin))
            continue
            
            if pin == self.pin:
                navigation = input('What would you like to do today? Balance, Deposit, Withdrawal, Pay Bill? b/d/w/pb')
                if navigation == input('b'):
                    user.account_balance()
                elif navigation == input('d'):
                    user.account_deposit()
                elif navigation == input('w'):
                    user.account_deposit()
                elif navigation == input('pb'):
                    user.account_bill_pay()
            else:
                def end_program():
                    end = (input('Is there anything else you would like to do? Y/N'))
                    if end == 'Y':
                        program_run == True
                    else:
                        program_run == False

                

# while program_run == True:
#     if input("What is your pin? \n\t") == user_one.pin:
#         navigation = input('What would you like to do? Balance, Deposit, Withdrawal, Pay Bill? b/d/w/pb')
#         if navigation == 'b':
#             user_one.account_balance()
#         elif navigation == 'd':
#             user_one.account_deposit(int(input('How much would you like to deposit into your account?\n\t')))
#         elif navigation == 'w':
#             user_one.account_withdrawal(int(input('How much would you like to withdraw from your account?')))
#         elif navigation == 'pb':
#             user_one.account_bill_pay(input('Who are we making a payment to?\n\t')), int(input('How much would you like to pay?'))
#         else:
#             print( f'Wrong pin number, please try again')
#             program_run == False

            

