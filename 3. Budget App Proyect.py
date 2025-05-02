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
        balance = sum(item["amount"] for item in self.ledger)
        return balance
        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()
        
    def __str__(self):
        # Title centered with asterisks
        title = f"{self.name:*^30}\n"
        
        # Ledger items formatted
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
            
        # Total balance
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total
        
def create_spend_chart(categories):
    # Calculate total and each category's spent amount
    category_spent = []
    total_spent = 0

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spent.append(spent)
        total_spent += spent

    # Calculate percentage spent for each category (rounded down to nearest 10)
    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in category_spent]

    # Build the chart string
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "  # Right-align numbers and add '|'
        for percent in percentages:
            chart += "o  " if percent >= i else "   "  # Add 'o' if percent meets level, else blank space
        chart += "\n"

    # Add the bottom line separator
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Determine the longest category name length
    max_name_len = max(len(category.name) for category in categories)

    # Add category names vertically
    for i in range(max_name_len):
        chart += "     "  # Left padding for alignment
        for category in categories:
            chart += (category.name[i] + "  ") if i < len(category.name) else "   "
        chart += "\n"

    return chart.rstrip("\n")  # Remove extra newline at the end