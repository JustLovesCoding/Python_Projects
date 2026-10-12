class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self,amount, optional_des=""):
        self.amount = amount
        self.optional_des = optional_des
        self.ledger.append({"amount": amount, "description": optional_des})

    def withdraw(self,amount,optional_des=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": optional_des})
            return True
        else:
            return False
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
    def get_balance(self):
        self.balance = 0
        for transaction in self.ledger:
            self.balance += transaction["amount"]
        return self.balance
    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for transaction in self.ledger:
            amount = f"{transaction['amount']:.2f}"
            description = transaction['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = 0
    spent_per_category = []
    for category in categories:
        spent = sum(-transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0)
        spent_per_category.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spent_per_category]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            chart += f"{category.name[i] if i < len(category.name) else ' '}  "
        chart += "\n"

    return chart.rstrip("\n")
    

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15)
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food.get_balance())
print(clothing.get_balance())
print(food.withdraw(100, 'groceries'))
print(food)
print(create_spend_chart([food, clothing]))