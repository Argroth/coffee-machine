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

    #check remaining stocks before making a coffee
    def checkRemainingStock(self, coffeToMake):
        #get coffee to check ingredients
        coffeIngredients = coffeeMenu[coffeToMake]

        if(coffeIngredients["water"] < self.water or coffeIngredients["coffee"] < self.coffee or coffeIngredients["milk"] < self.milk):
            print("Za mało składników!")
        # print(coffeIngredients)
        print(f"resources left coffee: {self.coffee}, milk: {self.milk}, water: {self.water}")

    #make coffee
    def makeCoffee(self, coffeeToMake):
        print(f"Making coffee: {coffeeToMake}")

#Define coffee machine menu
coffeeMenu = {
    "latte": {
        "water": 50,
        "coffee": 20,
        "milk": 150,
        "price": 1.4
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
coffeeMachine = CoffeeMachine(10, 500, 500, 5)

print(coffeeMenu)
x = input("Podaj co robić: ")
if(x == "stock"):
    coffeeMachine.printStatus()
elif(x == "coffee"):
    coffeToMake = input("Jaką kawę zrobić? ")
    coffeeMachine.checkRemainingStock(coffeToMake)
    # coffeeMachine.makeCoffee(coffeToMake)

#
#
# coffeeMachine.printStatus()
#
# coffeeMachine.makeCoffee("Cappucino")
