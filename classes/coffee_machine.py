import sys

# The resources are: "water", "milk", "beans", "cups", "money"
# The supported products are: "espresso", "latte", "cappucino"
# The supported actions are: "buy", "fill", "take", "remaining", "exit"

class CoffeeMachine:
    def __init__(self, default_resources=None):
        if default_resources is None:
            default_resources = [400, 540, 120, 9, 550]
        self.resources = default_resources
        self.actions = ["buy", "fill", "take", "remaining", "exit"]
        self.products = {
            "1": ["espresso", [250, 0, 16, 4]], 
            "2": ["latte", [350, 75, 20, 7]], 
            "3": ["cappuccino", [200, 100, 12, 6]]
        }
    
    def exit(self):
        sys.exit()

    def fill(self):
        self.resources[0] += int(input("Write how many ml of water do you want to add:\n"))
        self.resources[1] += int(input("Write how many ml of milk do you want to add:\n"))
        self.resources[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.resources[3] += int(input("Write how many disposable cups do you want to add:\n"))

    def remaining(self):
        print(f"""
        The coffee machine has:\n
        {self.resources[0]} of water\n
        {self.resources[1]} of milk\n
        {self.resources[2]} of coffee beans\n
        {self.resources[3]} of disposable cups\n
        ${self.resources[4]} of money\n""")

    def take(self):
        print(f"I gave you ${self.resources[4]}")
        self.resources[4] = 0

    def check_ingredients(self, choice):
        if self.products[choice][1][0] > self.resources[0]:
            return "water"
        if self.products[choice][1][1] > self.resources[1]:
            return "milk"
        if self.products[choice][1][2] > self.resources[2]:
            return "beans"
        return True

    def make(self, choice):
        self.resources[0] -= self.products[choice][1][0]
        self.resources[1] -= self.products[choice][1][1]
        self.resources[2] -= self.products[choice][1][2]
        self.resources[4] += self.products[choice][1][3]

    def buy(self):
        choice = input("What do you want to buy [type 'back' to cancel]? '1' - espresso, '2' - latte, '3' - cappuccino:\n")
        
        if choice != "back":
            if "1" <= choice <= "3":
                ingredients = self.check_ingredients(choice)
                if ingredients == True:
                    print("I have enough resources, making you a coffee!")
                    self.resources[3] -= 1
                    self.make(choice)
                else:
                    print(f"Sorry, not enough {ingredients}!")
            else:
                print(f"{choice} is unsupported")  

    def main(self): 
        while True:
            print("Write action ('buy', 'fill', 'take', 'remaining', 'exit'):")
            desired_action = input().lower()
            if desired_action in self.actions:
                eval("self." + desired_action + "()")
            else:
                print(f"{desired_action} is unsupported")

    def __repr__(self):
        return "Resources({}ml, {}ml, {}g, {}, {}$)".format(
            self.resources[0], 
            self.resources[1], 
            self.resources[2], 
            self.resources[3], 
            self.resources[4]
        )

    def __str__(self):
        return """
        Current resources: {} ml water, {} ml milk, {} g beans, {} cups. 
        Current money: ${}.
        Supported products: 
        >>> {} - ${} ({} ml water, {} ml milk, {} g beans)
        >>> {} - ${} ({} ml water, {} ml milk, {} g beans)
        >>> {} - ${} ({} ml water, {} ml milk, {} g beans)
        """.format(
            self.resources[0], 
            self.resources[1], 
            self.resources[2], 
            self.resources[3], 
            self.resources[4],
            self.products["1"][0],
            self.products["1"][1][3],
            self.products["1"][1][0],
            self.products["1"][1][1],
            self.products["1"][1][2],
            self.products["2"][0],
            self.products["2"][1][3],
            self.products["2"][1][0],
            self.products["2"][1][1],
            self.products["2"][1][2],
            self.products["3"][0],
            self.products["3"][1][3],
            self.products["3"][1][0],
            self.products["3"][1][1],
            self.products["3"][1][2]
            )