from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, current_balance, account_number, routing_number):
        super().__init__(current_balance)
        self.transfer_count = 0
        self.transfer_limitation = 5
        self._account_number = account_number  # one underscore for protected
        self.__routing_number = routing_number  # two underscore for private

    def transfer(self, amount):
        if self.transfer_count >= self.transfer_limitation:
            print("Sorry you have reached the limit of transfer!")

        if amount > self.current_balance:
            print("There are insufficient funds")
            return #need this as it stops the method

        self.transfer_count += 1
        self.current_balance -= amount
        print("Your money was successfully transferred! Your remaining balance is: ", self.current_balance)

