from BankAccount import BankAccount
#need protected & private members account number, routing number
#savings account with interest

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._account_number = account_number #one underscore for protected
        self.__routing_number = routing_number #two underscore for private

    def interestRate(self):
        interest = self.current_balance * 0.25
        print("Your new balance with the added interest rate is: ", interest)
