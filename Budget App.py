class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line: 30 chars, name centered with *
        output = self.name.center(30, "*") + "\n"
        
        # Ledger items
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = "{:.2f}".format(item["amount"]).rjust(7)
            output += f"{desc}{amt}\n"
            
        # Total line
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    # 1. Calculate spending per category (withdrawals only)
    spent_amounts = []
    for cat in categories:
        spent = sum(abs(item["amount"]) for item in cat.ledger if item["amount"] < 0)
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    
    # Calculate percentages rounded down to the nearest 10
    # To avoid division by zero if nothing was spent
    percentages = []
    for amount in spent_amounts:
        if total_spent > 0:
            percentages.append(int((amount / total_spent) * 100 // 10) * 10)
        else:
            percentages.append(0)

    # 2. Build the chart top-down
    res = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    # 3. Horizontal line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Vertical names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]

    for i in range(max_len):
        res += "     "
        for name in names:
            res += name[i] + "  "
        if i < max_len - 1:
            res += "\n"

    return res