class CoffeeMachine:
    income = 0

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
        calculateIncome(currentCoffee['price'] - currentCoffee['cost'])

        print(f"Making coffee: {coffeeToMake}")
        print(f"Price: {currentCoffee['price']}")


def calculateIncome(income):
    print(f"Income: {round(income, 3)}")


def generateMachines(n):
    instances = [CoffeeMachine(500, 500, 500, 200) for i in range(n)]
    for i in range(n):
        print(instances[i].income)


# Define coffee machine menu
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

# generateMachines(10)
# # create new instance of Coffee Machine: coffee, milk, water, money
coffeeMachine = CoffeeMachine(1000, 500, 500, 10)
#
# # x = input("Podaj co robić: ")
x = "coffee"
y = "latte"
z = 4
if x == "stock":
    coffeeMachine.printStatus()
elif x == "coffee":
    # coffeeToMake = input("Jaką kawę zrobić? ")
    if not coffeeMachine.checkRemainingStock(y):
        coffeeMachine.makeCoffee(y, z)
        coffeeMachine.printStatus()

# TODO add menu
# TODO add alerts for low stocks
# TODO add income + tax
# TODO calculate effectiveness
# TODO create report
# TODO add stock to instance
# TODO add collect income
# TODO add progress bar
# TODO add customer generator
# coffeeMachine.printStatus()
#
# coffeeMachine.makeCoffee("Cappucino")
