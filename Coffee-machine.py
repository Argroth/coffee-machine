import time
import gc
from tabulate import tabulate
from tqdm import tqdm

machines = []


class CoffeeMachine:
    income = 0
    coffeesMade = 0

    def __init__(self, coffee, milk, water, money):
        self.id = (len(machines))
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.money = money

    # print status of current resources
    def printStatus(self):
        print(f"Coffee left: {self.coffee}")
        print(f"Milk left: {self.milk}")
        print(f"Water left: {self.water}")
        print(f"Money left: {self.money}")

    # check remaining stocks before making a coffee
    def checkRemainingStock(self, coffee):
        # get coffee to check ingredients
        coffeeIngredients = coffeeMenu[coffee]

        # checking ingredients and printing results if there is not enough resources in stock
        if coffeeIngredients["water"] > self.water or coffeeIngredients["coffee"] > self.coffee or \
                coffeeIngredients["milk"] > self.milk:
            print("No ingredients!")
            return True
        return False

    # make coffee
    def makeCoffee(self, coffee, insertedCoin):
        currentCoffee = coffeeMenu[coffee]
        self.coffee = self.coffee - currentCoffee['coffee']
        self.water = self.water - currentCoffee['water']
        self.milk = self.milk - currentCoffee['milk']
        self.money = self.money + (insertedCoin - currentCoffee['price'])
        self.coffeesMade += 1

        self.calculateIncome(currentCoffee['price'] - currentCoffee['cost'])

        print(f"Making coffee: {coffee}")
        for i in tqdm(range(100)):
            time.sleep(0.008)

        print(f"Price: {currentCoffee['price']}")
        print(f"Change: {insertedCoin - currentCoffee['price']}")

    # calculate income for specific machine
    def calculateIncome(self, machineIncome):
        self.income = self.income + round(machineIncome, 3)


coffeeMenu = {
    "black": {
        "water": 2000,
        "coffee": 1,
        "milk": 1,
        "price": 1.4,
        "cost": 0.7
    },

    "cappuccino": {
        "water": 50,
        "coffee": 20,
        "milk": 150,
        "price": 1.2,
        "cost": 0.7
    },

    "latte": {
        "water": 50,
        "coffee": 20,
        "milk": 150,
        "price": 1.4,
        "cost": 0.4
    }
}


# init one machine
machines.append(CoffeeMachine(1000, 500, 500, 10))

# menu
answer = True
while answer:
    print(f"""
    Welcome to BasicCoffee. Currently we have {len(machines)} working machine(s).
    1.  Make a coffee
    2.  Check Status
    3.  Collect Income
    9.  Install new machine
    ---
    Q.  Quit
    """)
    answer = input("Choose option: ")
    # make a coffee
    if answer == "1":
        table = []

        print("Available coffee machines: ")
        for obj in gc.get_objects():
            if isinstance(obj, CoffeeMachine):
                table.append(obj.__dict__)

        print(tabulate(table, headers="keys"))
        machine = int(input("Choose Coffee Machine: "))
        print(machines[machine])

        moneyInserted = int(input("Please insert money! "))

        print("Menu: ")
        for drink in coffeeMenu:
            print(drink)

        coffeeToMake = input("What do you want to drink? ")
        if not machines[machine].checkRemainingStock(coffeeToMake):
            machines[machine].makeCoffee(coffeeToMake, moneyInserted)

    # print status of specific machine
    elif answer == "2":
        table = []
        incomeAllMachines = 0
        for obj in gc.get_objects():
            if isinstance(obj, CoffeeMachine):
                table.append(obj.__dict__)
                incomeAllMachines = incomeAllMachines + obj.income

        print(tabulate(table, headers="keys"))
        print(f"Income: {incomeAllMachines}")

    # collect income across all machines
    elif answer == "3":
        income = 0
        for obj in gc.get_objects():
            if isinstance(obj, CoffeeMachine):
                income = income + obj.income

        print(f"Current income across all coffee machines: {income}")

    # create new machine
    elif answer == "9":
        machines.append(CoffeeMachine(222, 666, 555, 100))

    elif answer == "Q" or answer == "q":
        print("\n Goodbye")
        answer = None
    else:
        print("\n Not Valid Choice Try again")
