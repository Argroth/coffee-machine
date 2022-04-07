import time
from tqdm import tqdm


class CoffeeMachine:
    income = 0
    coffeesMade = 0

    def __init__(self, coffee, milk, water, money):
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

    def calculateIncome(self, income):
        self.income = self.income + round(income, 3)


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

coffeeMachine = CoffeeMachine(1000, 500, 500, 10)

answer = True
while answer:
    print("""
    1.  Make a coffee
    2.  Check Status
    3.  Collect Income
    Q.  Quit
    """)
    answer = input("Choose option: ")
    if answer == "1":
        moneyInserted = int(input("Please insert money! "))
        coffeeToMake = input("What do you want to drink? ")
        if not coffeeMachine.checkRemainingStock(coffeeToMake):
            coffeeMachine.makeCoffee(coffeeToMake, moneyInserted)

    elif answer == "2":
        print(coffeeMachine.printStatus())

    elif answer == "3":
        print("\n Collecting income...")
        print(f"Collected income: {coffeeMachine.income}")
        coffeeMachine.income = 0

    elif answer == "Q" or answer == "q":
        print("\n Goodbye")
        answer = None
    else:
        print("\n Not Valid Choice Try again")
