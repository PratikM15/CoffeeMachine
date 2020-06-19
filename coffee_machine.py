# Write your code here
class CoffeeMachine:
    
    def __init__(self, water, milk, beans, disposable, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable = disposable
        self.money = money

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "ml of milk")
        print(self.beans, "g of coffee beans")
        print(self.disposable, "of disposable cups")
        print(self.money, "$ of money")
        print()

    def buy(self, number):

        if self.disposable == 0:
            print("Sorry, not enough disposable cups!")
        
        elif number == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough beans!")
            else:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.disposable -= 1
                print("I have enough resources, making you a coffee!")
        
        elif number == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough beans!")
            else:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.disposable -= 1
                print("I have enough resources, making you a coffee!")
                
        elif number == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough beans!")
            else:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.disposable -= 1
                print("I have enough resources, making you a coffee!")
        
        elif number == "back":
            pass

        else:
            pass
        print()
        
    def fill(self, water, milk, beans, disposable):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.disposable += disposable       
        print()
    
    def take(self):
        print("I gave you $"+str(self.money))
        self.money = 0
        print()

coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print()
    if action == 'buy':
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        number = input()
        coffee_machine.buy(number)
    elif action == 'take':
        coffee_machine.take()
    elif action == 'fill':
        print("Write how many ml of water do you want to add:")
        water = int(input())
        print("Write how many ml of milk do you want to add:")
        milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        disposable = int(input())
        coffee_machine.fill(water, milk, beans, disposable)
    elif action == 'remaining':
        coffee_machine.remaining()
    elif action == 'exit':
        break
    else:
        print("Please enter valid choice.")
        print()
    
            
    
    
