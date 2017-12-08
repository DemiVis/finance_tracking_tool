

class Expense:
    """
    A class to encapsulate the information for a single expense.

    all data members are public and therefore no set or get functions needed
    """

    def __init__(self, description, amount, account, date, category):
        self.description = description
        self.amount = amount
        self.account = account
        self.date = date
        self.category = category
