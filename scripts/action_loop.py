import sys

# Description
# Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. 
# It should repeatedly ask a user what they want to do. If the user types "buy", "fill" or "take", 
# then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, 
# they should type "exit". The program should terminate on this command. Also, when the user types "remaining", 
# the program should output all the resources that the coffee machine has.
#
# Objectives
# Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. 
# Introduce two new options: "remaining" and "exit".
# Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, 
# the program should output a message that says it can't make a cup of coffee.
# And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, 
# they should be able to type "back" to return into the main cycle.
#
# Examples
# Your coffee machine should have the the same initial resources as in the example:
# 400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash.
# The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
#
# Example 1:
# Write action (buy, fill, take, remaining, exit):
# > remaining
# The coffee machine has:
# 400 of water
# 540 of milk
# 120 of coffee beans
# 9 of disposable cups
# $550 of money
# Write action (buy, fill, take, remaining, exit):
# > buy
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
# > 2
# I have enough resources, making you a coffee!
# Write action (buy, fill, take, remaining, exit):
# > remaining
# The coffee machine has:
# 50 of water
# 465 of milk
# 100 of coffee beans
# 8 of disposable cups
# $557 of money
# Write action (buy, fill, take, remaining, exit):
# > buy
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
# > 2
# Sorry, not enough water!
# Write action (buy, fill, take, remaining, exit):
# > fill
# Write how many ml of water do you want to add:
# > 1000
# Write how many ml of milk do you want to add:
# > 0
# Write how many grams of coffee beans do you want to add:
# > 0
# Write how many disposable cups of coffee do you want to add:
# > 0
# Write action (buy, fill, take, remaining, exit):
# > remaining
# The coffee machine has:
# 1050 of water
# 465 of milk
# 100 of coffee beans
# 8 of disposable cups
# $557 of money
# Write action (buy, fill, take, remaining, exit):
# > buy
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
# > 2
# I have enough resources, making you a coffee!
# Write action (buy, fill, take, remaining, exit):
# > remaining
# The coffee machine has:
# 700 of water
# 390 of milk
# 80 of coffee beans
# 7 of disposable cups
# $564 of money
# Write action (buy, fill, take, remaining, exit):
# > take
# I gave you $564
# Write action (buy, fill, take, remaining, exit):
# > remaining
# The coffee machine has:
# 700 of water
# 390 of milk
# 80 of coffee beans
# 7 of disposable cups
# 0 of money
# Write action (buy, fill, take, remaining, exit):
# > exit

actions = ["buy", "fill", "take", "remaining", "exit"]
products = ["espresso", "latte", "cappucino"]
espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappucino = [200, 100, 12, 6]

def fill_default_ingredients():
    global water
    global milk
    global beans
    global cups
    global money

    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

def input_ingredients():
    global water
    global milk
    global beans
    global cups
    global money

    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    cups = int(input("Write how many disposable cups the coffee machine has:\n"))
    money = int(input("Write how many money the coffee machine has:\n"))

def make_espresso():
    global water
    global milk
    global beans
    global money

    water -= espresso[0]
    milk -= espresso[1]
    beans -= espresso[2]
    money += espresso[3]

def make_latte():
    global water
    global milk
    global beans
    global money

    water -= latte[0]
    milk -= latte[1]
    beans -= latte[2]
    money += latte[3]

def make_cappucino():
    global water
    global milk
    global beans
    global money

    water -= cappucino[0]
    milk -= cappucino[1]
    beans -= cappucino[2]
    money += cappucino[3]

def buy():
    product_index = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    
    if 1 <= product_index <= 3:
        global cups
        cups -= 1
        eval("make_" + (products[product_index - 1]) + "()")
    else:
        print(f"{product_index} is unsupported")    

def fill():
    global water
    global milk
    global beans
    global cups

    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups do you want to add:\n"))

def take():
    global money
    print(f"I gave you ${money}")
    money = 0

def remaining():
    print("The coffee machine has:\n")
    print(f"{water} of water\n")
    print(f"{milk} of milk\n")
    print(f"{beans} of coffee beans\n")
    print(f"{cups} of disposable cups\n")
    print(f"{money} of money\n")

def exit():
    sys.exit()

def main(): 
    print("Write action (buy, fill, take, remaining, exit):")
    desired_action = input().lower()
    
    while desired_action != "exit":
        if desired_action in actions:
            eval(desired_action + "()")
        else:
            print(f"{desired_action} is unsupported")
        print("Write action (buy, fill, take, remaining, exit):")
        desired_action = input().lower()
    exit()

fill_default_ingredients()
main()
