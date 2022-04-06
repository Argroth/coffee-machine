class CoffeeMachine:
   def __init__(self, coffee, milk, water):
    self.coffee = coffee
    self.milk = milk
    self.water = water

    def printStatus(self):
        print("Coffee left: ", self.coffee)
        print("Milk left: ", self.milk)
        print("Water left: ", self.water)

coffeeMachine = CoffeeMachine("100", "500", "500")

print(coffeeMachine.printStatus())