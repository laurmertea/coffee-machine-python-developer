# Description
# Now let's consider a case when you need a lot of coffee. 
# Maybe you're hosting a party with a lot of guests! In these circumstances, 
# it's better to make preparations in advance.
# So, we will ask a user to enter the desired amount of coffee, in cups. 
# Given this, you can adjust the program by calculating 
# how much water, coffee, and milk are necessary to make the specified amount of coffee.
# Of course, all this coffee is not needed right now, so at this stage, 
# the coffee machine doesn't actually make any coffee yet.
#
# Objectives
# Let's break the task into several steps:
# First, read the numbers of coffee drinks from the input.
# Figure out how much of each ingredient the machine will need. 
# Note that one cup of coffee made on this coffee machine 
# contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
# Output the required ingredient amounts back to the user.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.
# 
# Example 1: a dialogue with a user might look like this
# Write how many cups of coffee you will need:
# > 25
# For 25 cups of coffee you will need:
# 5000 ml of water
# 1250 ml of milk
# 375 g of coffee beans
# 
# Example 2: here is another dialogue
# Write how many cups of coffee you will need:
# > 125
# For 125 cups of coffee you will need:
# 25000 ml of water
# 6250 ml of milk
# 1875 g of coffee beans

ingredients = [200, 50, 15]
cups_number = int(input("Write how many cups of coffee you will need:"))

water = cups_number * ingredients[0]
milk = cups_number * ingredients[1]
beans = cups_number * ingredients[2]

print(f"""For {cups_number} cups of coffee you will need:
    {water} ml of water
    {milk} ml of milk
    {beans} g of coffee beans.W""")