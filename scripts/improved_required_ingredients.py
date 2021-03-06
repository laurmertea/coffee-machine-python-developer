# Description
# A real coffee machine doesn't have an infinite supply of water, milk, or coffee beans. 
# And if you input a really big number, it's almost certain that a real coffee machine 
# wouldn't have the supplies needed to make all that coffee for you.
# In this stage, you need to improve the previous program. 
# Now you will check amounts of water, milk, and coffee beans available 
# in your coffee machine at the moment.
#
# Objectives
# Write a program that does the following:
# It requests the amounts of water, milk, and coffee beans available at the moment, 
# and then asks for the number of cups a user needs.
# If the coffee machine has enough supplies to make the specified amount of coffee, 
# the program should print "Yes, I can make that amount of coffee".
# If the coffee machine can make more than that, 
# the program should output "Yes, I can make that amount of coffee (and even N more than that)", 
# where N is the number of additional cups of coffee that the coffee machine can make.
# If the amount of given resources is not enough to make the specified amount of coffee, 
# the program should output "No, I can make only N cups of coffee".
# Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, 
# and 15 g of coffee beans to make one cup of coffee.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.
# 
# Example 1:
# Write how many ml of water the coffee machine has:
# > 300
# Write how many ml of milk the coffee machine has:
# > 65
# Write how many grams of coffee beans the coffee machine has:
# > 100
# Write how many cups of coffee you will need:
# > 1
# Yes, I can make that amount of coffee
# 
# Example 2:
# Write how many ml of water the coffee machine has:
# > 500
# Write how many ml of milk the coffee machine has:
# > 250
# Write how many grams of coffee beans the coffee machine has:
# > 200
# Write how many cups of coffee you will need:
# > 10
# No, I can make only 2 cups of coffee
#
# Example 3:
# Write how many ml of water the coffee machine has:
# > 1550
# Write how many ml of milk the coffee machine has:
# > 299
# Write how many grams of coffee beans the coffee machine has:
# > 300
# Write how many cups of coffee you will need:
# > 3
# Yes, I can make that amount of coffee (and even 2 more than that)
#
# Example 4:
# Write how many ml of water the coffee machine has:
# > 0
# Write how many ml of milk the coffee machine has:
# > 0
# Write how many grams of coffee beans the coffee machine has:
# > 0
# Write how many cups of coffee you will need:
# > 1
# No, I can make only 0 cups of coffee
#
# Example 5:
# Write how many ml of water the coffee machine has:
# > 0
# Write how many ml of milk the coffee machine has:
# > 0
# Write how many grams of coffee beans the coffee machine has:
# > 0
# Write how many cups of coffee you will need:
# > 0
# Yes, I can make that amount of coffee
#
# Example 6:
# Write how many ml of water the coffee machine has:
# > 200
# Write how many ml of milk the coffee machine has:
# > 50
# Write how many grams of coffee beans the coffee machine has:
# > 15
# Write how many cups of coffee you will need:
# > 0
# Yes, I can make that amount of coffee (and even 1 more than that)

ingredients = [200, 50, 15]

def calc_water(cups_number):
    return cups_number * ingredients[0]

def calc_milk(cups_number):
    return cups_number * ingredients[1]

def calc_beans(cups_number):
    return cups_number * ingredients[2]

def calc_max_cups_by_ingredients():
    return [max_water // ingredients[0], max_milk // ingredients[1], max_beans // ingredients[2]]

def calc_max_cups_number():
    return min(calc_max_cups_by_ingredients())

max_water = int(input("Write how many ml of water the coffee machine has:\n"))
max_milk = int(input("Write how many ml of milk the coffee machine has:\n"))
max_beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups_number = int(input("Write how many cups of coffee you will need:\n"))
max_cups = calc_max_cups_number()

if (cups_number == max_cups):
    print("Yes, I can make that amount of coffee")
elif (cups_number < max_cups):
    additional = max_cups - cups_number
    print(f"Yes, I can make that amount of coffee (and even {additional} more than that)")
else:
    print(f"No, I can make only {max_cups} cups of coffee")
