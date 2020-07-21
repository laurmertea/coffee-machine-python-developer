# Description
# Let's simulate an actual coffee machine! What do we need for that? 
# This coffee machine will have a limited supply of water, milk, coffee beans, and disposable cups. 
# Also, it will calculate how much money it gets for selling coffee.
# There are several options for the coffee machine we want you to implement: first, it should sell coffee. 
# It can make different types of coffee: espresso, latte, and cappuccino. 
# Of course, each variety requires a different amount of supplies, however, 
# in any case, you will need only one disposable cup for a drink. 
# Second, the coffee machine must get replenished by a special worker. 
# Third, another special worker should be able to take out money from the coffee machine.
#
# Objectives
# Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. 
# Note that the program is supposed to do one of the mentioned actions at a time. 
# It should also calculate how many ingredients and money have left. 
# Display the number of supplies before and after purchase.
# First, your program reads one option from the standard input, which can be "buy", "fill", "take". 
# If a user wants to buy some coffee, the input is "buy". 
# If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be "fill". 
# If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input "take".
# If the user writes "buy" then they must choose one of three types of coffee 
# that the coffee machine can make: espresso, latte, or cappuccino.
# For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
# For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
# And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
# If the user writes "fill", the program should ask them how much water, milk, coffee 
# and how many disposable cups they want to add into the coffee machine.
# If the user writes "take" the program should give all the money that it earned from selling coffee.
# At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
# To sum up, your program should print the coffee machine's state, process one query from the user, 
# as well as print the coffee machine's state after that. 
# Try to use functions for implementing every action that the coffee machine can do.
#
# Examples
# An espresso should be as number 1 in the list, a latte as number 2 and a cappuccino as number 3.
# Options are named as "buy", "fill", "take".
# The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
#
# Example 1:
# The coffee machine has:
# 400 of water
# 540 of milk
# 120 of coffee beans
# 9 of disposable cups
# 550 of money
# Write action (buy, fill, take):
# > buy
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:
# > 3
# The coffee machine has:
# 200 of water
# 440 of milk
# 108 of coffee beans
# 8 of disposable cups
# 556 of money
#
# Example 2:
# The coffee machine has:
# 400 of water
# 540 of milk
# 120 of coffee beans
# 9 of disposable cups
# 550 of money
# Write action (buy, fill, take):
# > fill
# Write how many ml of water do you want to add:
# > 2000
# Write how many ml of milk do you want to add:
# > 500
# Write how many grams of coffee beans do you want to add:
# > 100
# Write how many disposable cups of coffee do you want to add:
# > 10
# The coffee machine has:
# 2400 of water
# 1040 of milk
# 220 of coffee beans
# 19 of disposable cups
# 550 of money
#
# Example 3:
# The coffee machine has:
# 400 of water
# 540 of milk
# 120 of coffee beans
# 9 of disposable cups
# 550 of money 
# Write action (buy, fill, take):
# > take
# I gave you $550
# The coffee machine has:
# 400 of water
# 540 of milk
# 120 of coffee beans
# 9 of disposable cups
# 0 of money

actions = ["buy", "fill", "take"]
products = ["espresso", "latte", "cappucino"]
espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappucino = [200, 100, 12, 6]

def ingredients():
    print("The coffee machine has:\n")
    print(f"{water} of water\n")
    print(f"{milk} of milk\n")
    print(f"{beans} of coffee beans\n")
    print(f"{cups} of disposable cups\n")
    print(f"{money} of money\n")

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

def main():
    ingredients()
    print("Write action (buy, fill, take):")
    desired_action = input().lower()
    
    if desired_action in actions:
        eval(desired_action + "()")
        ingredients()
    else:
        print(f"{desired_action} is unsupported")

water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups = int(input("Write how many disposable cups the coffee machine has:\n"))
money = int(input("Write how many money the coffee machine has:\n"))

main()
