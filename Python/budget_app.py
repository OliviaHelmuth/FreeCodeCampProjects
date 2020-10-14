class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.current_balance = 0
        self.total_withdraw = 0

    def __str__(self):
        line = '{:*^30}\n'.format(self.name)
        for item in self.ledger:
            line += '{:<23}{:>7.2f}\n'.format(
                item['description'][:23], item['amount'])

        line += "Total: {:.2f}".format(self.current_balance)
        return line

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.current_balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": - amount, "description": description})
            self.current_balance -= amount
            self.total_withdraw += amount
            return True
        return False

    def get_balance(self):
        return self.current_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        return self.current_balance >= amount


def create_spend_chart(categories):

    total_withdraw = 0
    spend_arr = []

    for item in categories:
        total_withdraw += item.total_withdraw
        spend_arr.append([item.name, item.total_withdraw])

    for item in spend_arr:
        item[1] = int(100 * item[1] / total_withdraw)

    format_chart(spend_arr)


def format_chart(spend_arr):

    percent = 100
    line = "Percentage spent by category\n"

    cats = [item[0] for item in spend_arr]

    biggest_size = len(max(cats, key=len))

    while percent >= 0:
        line += "{:>3}|".format(percent)
        for item in spend_arr:
            o = draw_o(percent, item[1])
            line += " {o} ".format(o=o)
        percent -= 10
        line += '\n'

    line += "    " + "-"*(3 * len(cats)) + "-\n"

    for i in range(biggest_size):
        line += "   "
        for letter in spend_arr:
            try:
                line += "  " + letter[0][i]
            except:
                line += "   "

        line += "\n"

    return line


def draw_o(percent, spend_arr):
    if percent <= spend_arr:
        return "o"
    return " "
