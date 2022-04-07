import os
import time
import pymongo
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

# print(os.environ.get('DB_URL'))

# DB config
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
dbName = myClient["CoffeeMachine"]
dbCoffeeMenu = dbName["CoffeeMenu"]


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
        print(f"Income: {self.income}")
        print(f"Coffees Made: {self.coffeesMade}")
        print(f"Coffee left: {self.coffee}")
        print(f"Milk left: {self.milk}")
        print(f"Water left: {self.water}")
        print(f"Money left: {self.money}")

    # check remaining stocks before making a coffee
    def checkRemainingStock(self, coffeeToMake):
        # get coffee to check ingredients
        coffeeIngredients = coffeeMenu[coffeeToMake]

        # checking ingredients and printing results if there is not enough resources in stock
        if coffeeIngredients["water"] > self.water or coffeeIngredients["coffee"] > self.coffee or \
                coffeeIngredients["milk"] > self.milk:
            print("No ingredients!")
            return True
        return False

    # make coffee
    def makeCoffee(self, coffeeToMake, insertedCoin):
        currentCoffee = coffeeMenu[coffeeToMake]
        self.coffee = self.coffee - currentCoffee['coffee']
        self.water = self.water - currentCoffee['water']
        self.milk = self.milk - currentCoffee['milk']
        self.money = self.money + (insertedCoin - currentCoffee['price'])
        self.coffeesMade += 1

        self.calculateIncome(currentCoffee['price'] - currentCoffee['cost'])

        print(f"Making coffee: {coffeeToMake}")
        for i in tqdm(range(100)):
            time.sleep(0.001)
            # time.sleep(0.08)

        print(f"Price: {currentCoffee['price']}")
        print(f"Change: {insertedCoin - currentCoffee['price']}")

    def calculateIncome(self, income):
        self.income = self.income + round(income, 3)


def createNewCoffee(name, coffee, water, milk, price, cost):
    dbCoffeeMenu.insert_one({name: {"water": water, "coffee": coffee, "milk": milk, "price": price, "cost": cost}})


# Define coffee machine menu
# coffeeMenu = {
#     "black": {
#         "water": 2000,
#         "coffee": 1,
#         "milk": 1,
#         "price": 1.4,
#         "cost": 0.7
#     },
#
#     "cappuccino": {
#         "water": 50,
#         "coffee": 20,
#         "milk": 150,
#         "price": 1.2,
#         "cost": 0.7
#     },
#
#     "latte": {
#         "water": 50,
#         "coffee": 20,
#         "milk": 150,
#         "price": 1.4,
#         "cost": 0.4
#     }
# }

x = dbCoffeeMenu.find({'latte': {'$exists': 1}})

print(list(x))


# createNewCoffee("espresso", 150, 100, 0, 1, 0.5)
# createNewCoffee("latte", 50, 20, 150, 1.4, 0.4)
# createNewCoffee("black", 150, 20, 0, 1.2, 0.7)
# createNewCoffee("cappuccino", 150, 100, 0, 1.4, 0.4)
# coffeeMachine = CoffeeMachine(1000, 500, 500, 10)
# #
# # # x = input("Podaj co robić: ")
# x = "coffee"
# y = "latte"
# z = 4
# if x == "stock":
#     coffeeMachine.printStatus()
# elif x == "coffee":
#     # coffeeToMake = input("Jaką kawę zrobić? ")
#     if not coffeeMachine.checkRemainingStock(y):
#         coffeeMachine.makeCoffee(y, z)
#         coffeeMachine.printStatus()

# TODO add menu
# TODO add alerts for low stocks
# TODO add income + tax
# TODO calculate effectiveness
# TODO create report
# TODO add stock to instance
# TODO add collect income
# TODO add progress bar
# coffeeMachine.printStatus()
#
# coffeeMachine.makeCoffee("Cappucino")
