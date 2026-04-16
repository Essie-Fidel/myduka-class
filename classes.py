class person:
    def __init__(self, name, age, email, address):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def talk(self):
        print(f"{self.name} talks")

    def sleep(self):
        print(f"{self.name} is asleep")

    def code(self):
        print(f"{self.name} codes in python")


person1 = person("Jake", 25, 'jake@gmail.com', 'Bururburu Phase 1')
print(type(person1))
print(person1.age)
person1.talk()
person1.sleep()


person2 = person("Kate", 24, 'kate@gmail.com', 'Westlands')
print(type(person2))
print(person2.address)
person2.talk()
person2.sleep()
person2.code()


#    Task
class Bank_Account:
    def __init__(self, account_number, owner_name, balance, date_opened):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

    def deposit(self):
        print(f"{self.owner_name} has made a deposit")

    def withdraw(self):
        print(f"{self.owner_name} has made a withdrawal")

    def display_info(self):
        print(f"{self.owner_name} {self.account_number} {self.balance}")


Bank_Account1 = Bank_Account('B400987', "Oliver Smith", 980000, "2025-03-09")

print(type(Bank_Account1))
print(Bank_Account1.account_number)
Bank_Account1.deposit()
Bank_Account1.display_info()


Bank_Account2 = Bank_Account(
    'B600865', "Regina Williams", 876500, '2023/10/18')
print(type(Bank_Account2))
Bank_Account2.withdraw()
Bank_Account2.display_info()
