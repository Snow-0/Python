# Parent Class User
class User:

    def __init__(self, name, age, gender):
        self.age = age
        self.gender = gender
        self.name = name

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)


# Child Class Bank
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Your current balance is now $" + str(self.balance))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Your current balance is now $" + str(self.balance))
        print("Not enough funds to withdraw")

    def view_balance(self):
        print("$" + str(self.balance))

max = Bank("Max", 16, "Male")
max.show_details()
# max.deposit(100)
# max.view_balance()
# max.withdraw(101)
# max.view_balance()


