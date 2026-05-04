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


#    Task1
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
        print(
            f"Account details: {self.owner_name} {self.account_number} {self.balance}")


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

# task2
# Create a Car Class Have the following attributes brand - model - year - fuel_capcity - fuel_level - is_running(boolen value)
# Have the following methods as behaviour for your class: start() stop() refuel() drive() display_car_info()


class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            print(f"{self.brand} {self.model} has started")
        else:
            print(f"{self.brand} {self.model} cannot start; tank is empty")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped")
        else:
            print("Car is already stopped")

    def refuel(self, amount):
        if self.fuel_level + amount <= self.fuel_capacity:
            self.fuel_level += amount
            print(f"Refueled {amount}L. Fuel level: {self.fuel_level}L")
        else:
            print("Cannot exceed fuel capacity")

    def drive(self, distance):
        if not self.is_running:
            print("Start the car first")
        else:
            fuel_needed = distance
            if fuel_needed > self.fuel_level:
                print("Not enough fuel to drive")
            else:
                self.fuel_level -= fuel_needed
                print(
                    f"Drove {distance} km. Fuel left: {self.fuel_level:.2f}L")

    def display_info(self):
        print(f"""
Car Details:
Brand: {self.brand}
Model: {self.model}
Year: {self.year}
Fuel Capacity: {self.fuel_capacity}L
Fuel Level: {self.fuel_level}L
Running: {self.is_running}
""")


car1 = Car("Toyota", "Corolla", 2020, 50)

car1.start()
car1.refuel(20)
car1.start()
car1.drive(50)
car1.stop()
car1.display_info()

car2 = Car("Ford", "Ranger", 2023, 80)
car2.refuel(20)
car2.start()
car2.drive(4)
car2.stop()
