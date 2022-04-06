class CoffeeMachine:
    def __init__(self, coffee, milk, water, money):
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.money = money

    #print status of current resources
    def printStatus(self):
        print(f"Coffee left: {self.coffee}")
        print(f"Milk left: {self.milk}")
        print(f"Water left: {self.water}")
        print(f"Money left: {self.money}")

    #check remaining stocks before making a coffee
    def checkRemainingStock(self, coffeToMake):
        #get coffee to check ingredients
        coffeIngredients = coffeeMenu[coffeToMake]

        #checking ingredients and printing results if there is not enough resources in stock
        if(coffeIngredients["water"] < self.water or coffeIngredients["coffee"] < self.coffee or coffeIngredients["milk"] < self.milk):
            print("Za mało składników!")
            return True

        return "133"

    #make coffee
    def makeCoffee(self, coffeeToMake):
        print(f"Making coffee: {coffeeToMake}")

#Define coffee machine menu
coffeeMenu = {
    "latte": {
        "water": 1,
        "coffee": 1,
        "milk": 1,
        "price": 1
    },

    "cappucino": {
        "water": 50,
        "coffee": 20,
        "milk": 150,
        "price": 1.2
    },

    "black": {
        "water": 50,
        "coffee": 20,
        "milk": 150,
        "price": 0.8
    }
}

#create new instance of Coffee Machine: coffee, milk, water, money
coffeeMachine = CoffeeMachine(1000, 500, 500, 5)

print(coffeeMenu)
#x = input("Podaj co robić: ")
x = "coffee"
y = "latte"
if(x == "stock"):
    coffeeMachine.printStatus()
elif(x == "coffee"):
    #coffeToMake = input("Jaką kawę zrobić? ")
    print(coffeeMachine.checkRemainingStock(y))
    if(coffeeMachine.checkRemainingStock(y) == False):
        coffeeMachine.makeCoffee(coffeToMake)

#
#
# coffeeMachine.printStatus()
#
# coffeeMachine.makeCoffee("Cappucino")
