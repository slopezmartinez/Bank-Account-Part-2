class BankAccount:
    bank_title = 'The Two Sarahs Bank'

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print("Deposit", amount, "Updated Balance", str(self.current_balance))
        else:
            print("Deposit is not possible")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw not possible")
        elif self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print("Withdrew" + str(amount), "New Balance", str(self.current_balance))
        else:
            print("Withdraw is not possible")

    def print_customer_information(self):
        print("Bank", self.bank_title)
        print("Customer:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)
        

customer1 = BankAccount("Lopez", 12124, 203)
customer2 = BankAccount("Martinez", 15554, 100)

customer1.print_customer_information()
customer2.print_customer_information()

#Worked together with Sarah Santiago.





